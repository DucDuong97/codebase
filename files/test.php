<?php 

	namespace payroll;
	
	
	class Importer{
		
		public $verify_takehome=1;
		public $verify_account=1;
		public $dup = "skip";
		
		/**
		 * @desc Construct the importer
		 * @param Cycle $cycle
		 * @param CyclePolicy $cycle_policy
		 * @param \User $user
		 * @param \sys\System $system
		 */
		public function __construct($cycle, $cycle_policy, $user, $system){
			$this->cycle = $cycle;
			$this->cycle_policy = $cycle_policy;
			
			$this->user=$user;
			$this->system=$system;
			
			$this->_rks=[];
			for ($i=0; $i<count($this->cycle_policy->form); $i++){
				$this->_rks["k".$this->cycle_policy->form[$i]->id]=1;
			}
		}
		
		
		/**
		 * @desc Start the importing process
		 * @return \employee\Data\Contact[]
		 */
		public function start(){
			$this->verify_takehome = \HTML::inputCheckbox("verify_takehome");
			$this->verify_account = \HTML::inputCheckbox("verify_account");
			$this->dup = \HTML::inputInline("dup");
			
			
			$upload = new \base\Importer(["plain" => true, "array"=>false]);
			// Getting header is complex
			
			$headers = ["uid", "name", "salary", "basic_salary"];
			
			$this->addGroup($headers, "profile");
			$headers[] = "total_income";
			
			$this->addGroup($headers, "incomes");
			$this->addGroup($headers, "benefits");
			$this->addGroup($headers, "taxes");
			
			$this->addGroup($headers, "emp_insurances");
			$this->addGroup($headers, "emp_deductions");
			$headers[] = "takehome";
			
			$this->addGroup($headers, "company_insurances");
			$this->addGroup($headers, "company_extras");
			
			$headers[] = "company_total_costs";
			
			
			$upload->headerArray($headers);
			$upload->upload("file");
			
			if ($upload->hasError()) {
				\Ajax::release("FILE_ERROR");
				\Ajax::release($upload->getError());
			}
			
			$rows = $upload->getRows();
			if (!count($rows)){
				return [];
			}
			
			$rows = \ARR::filter($rows, function(&$e, $index){
				return $index>0 && $this->checkRow($e);
			});
			
			$done=[];
			for ($i=0; $i<count($rows); $i++){
				$r=$this->importRow($rows[$i]);
				
				if ($r){
					$done[]=$r;
				}
			}
			
			\Ajax::release(\Code::success("Successfully save ".count($done)." rows"));
		}
		
		
		/**
		 * @desc Import a single row
		 * @param mixed $row
		 */
		private function importRow($row){
			$e= $row->employee;
			if (!$e){
				\Ajax::release("ERROR_UNLOADING_{$row->uid}");
			}
			
			$r = Record::single("employee_id='{$e->id}' and cycle_policy_id='{$this->cycle_policy->id}'");
			
			if (!$r){
				$r=new Record();
				
				$r->employee($e);
				$r->cycle($this->cycle);
				$r->cyclePolicy($this->cycle_policy);
				
				if ($r->exist("employee_id, cycle_policy_id")){
					return false;
				}
			}else{
				if ($this->dup == "skip"){ // SKIP DUP
					return false;
				}
				
				$r->employee($e);
				$r->cycle($this->cycle);

			}
			
			if ($row->salary && \Valid::number($row->salary)){
				$r->profile->salary = \employee\importer\Parser::number($row->salary);
			}
			
			if ($row->basic_salary && \Valid::number($row->basic_salary)){
				$r->profile->basic_salary = \employee\importer\Parser::number($row->basic_salary);
			}
			
			$r->computed->total_income = $row->total_income;
			$this->setForm($r, $row);
			$r->recompute();
			
			if (!$r->save()){
				\Ajax::release(\Code::DB_ERROR);
			}
			
			return $r;
		}
		
		
		
		/**
		 * @desc Set employee profile into row
		 * @param object $row
		 * @return boolean
		 */
		private function checkRow(&$row){
			if (!$row->uid){
				return false;
			}
			
			if ($row->uid && !\Valid::number($row->total_income) || intval($row->total_income)<0){
				\Ajax::release("NO_TOTAL_INCOME_FOR_".$row->uid." ".safe($row->name));
			}
			
			$e=\employee\importer\Parser::employee($row->uid);
			if (!$e){
				\Ajax::release("NO_EMPLOYEE_FOR_".$row->uid." ".safe($row->name));
			}
			
			foreach ($row as $k=>$v){
				$v=str_replace([","], [""], "".$v);
				if ($this->isPayrollField($k)){
					if (\Valid::int($v)){
						$row->{$k} = intval($v);
					}else{
						$row->{$k} = floatval($v);
					}
				}
			}
			
			$row->employee=$e;
			
			$test=new Record();
			$test->employee($e);
			
			$test->computed->total_income = $row->total_income;
			$this->setForm($test, $row);
			$test->recompute();
			
			if ($this->verify_takehome){
				if (floatDiff($test->computed->emp_takehome, $row->takehome)){
					\Ajax::release("ERROR [{$row->uid}, {$row->name}]: EMPLOYEE_TAKEHOME_NOT_CORRECT, computed as {$test->computed->emp_takehome} vs input $row->takehome");
				}
			}
			
			return $row;
		}
		
		
		
		/**
		 * @desc Add a single group
		 */
		private function addGroup(&$headers, $type){
			for ($i=0; $i<count($this->cycle_policy->form); $i++){
				$row = $this->cycle_policy->form[$i];
				if ($row->group_id == $type){
					$headers[]=$row->id;
				}
			}
		}
	
		
		/**
		 * @desc Safely set form
		 * @param Record $r
		 * @param object $row
		 */
		private function setForm(&$r, $row){
			$form = $this->cycle_policy->form;
			
			for ($i=0; $i<count($form); $i++){
				$form[$i]->value=0;
				$form[$i]->display=0;
				
				$row_id=$form[$i]->id;
				if (!isset($row->{$row_id})){
				}else{
					$form[$i]->value=$row->{$row_id};
					$form[$i]->display=$row->{$row_id};
				}
			}
			
			
			$r->form = $form;
		}
		
		
		private function isPayrollField($key){
			return isset($this->_rks["k".$key]);
		}
		
	}
	

?>