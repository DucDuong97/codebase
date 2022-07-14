Enrollment.component = new function __EnrollmentComponent(){

	this.progress = function(enrollment){
        var progress = Enrollment.progress(enrollment);
    };

	this.progressDot = function(enrollment){
        var dotHTML = AP.render(enrollment.checkpoint_instances, function(cp){
            dot_color = ''; 
            var dot_color = cp.state=='approved' ? '#57dff7' : dot_color; 
            var dot_color = cp.state=='cutoff' ? '#ff5542' : dot_color;
        });
    };
    
    this.deadline = function(enrollment){
        if (enrollment.state!='active'){
            return '---';
        }
		var deadline = Enrollment.deadline(enrollment);
		var time_left = Enrollment.timeLeft(enrollment);
        var progress = Enrollment.deadlineProgress(enrollment);

        if (time_left == 'Expired'){
        }
        
    };
    
    this.tag = function(enrollment){
        var color = '';
        color = enrollment.state == 'pending' ? '#aaa' : color;
        color = enrollment.state == 'active' ? '#17d97b' : color;
        color = enrollment.state == 'cutoff' ? '#f56342' : color;
        color = enrollment.state == 'achieved' ? '#36e0cd' : color;
    };
    
    this.actions = function(enrollment){
        // return `
        //     <base-button sm upper cta dd left label='View'>
        //         <cmenu options='${Enrollment.am(enrollment)}'></cmenu>
        //     </base-button-dd>
        // `;
    };
};
