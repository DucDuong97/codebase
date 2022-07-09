Enrollment.component = new function __EnrollmentComponent(){

	this.progress = function(enrollment){
        var progress = Enrollment.progress(enrollment);
        return `
        asd`;
    };

	this.progressDot = function(enrollment){
        var dotHTML = AP.render(enrollment.checkpoint_instances, function(cp){
            dot_color = ''; 
            var dot_color = cp.state=='approved' ? '#57dff7' : dot_color; 
            var dot_color = cp.state=='cutoff' ? '#ff5542' : dot_color; 
            return `
                <base-dot style='display: inline-block;' edge color='${dot_color}'></base-dot>
            `;
        });
        return `
            <div class='enroll-progress-dot'>
                ${dotHTML}
            </div>
        `;
    };
    
    this.deadline = function(enrollment){
        if (enrollment.state!='active'){
            return '---';
        }
		var deadline = Enrollment.deadline(enrollment);
		var time_left = Enrollment.timeLeft(enrollment);
        var progress = Enrollment.deadlineProgress(enrollment);

        var figure = `<base-percent percent='${progress}'  size='30' solid bg='${Color.percent(100-parseInt(progress))}'></base-percent>`
        if (time_left == 'Expired'){
            figure = `
                <div style='position:absolute; top:8px; left: 14px'>
                    <base-shape square rounded color='danger' size='20'></base-shape>
                </div>
            `;
        }
        
        return `
            <div>
                ${figure}
                <div style='margin-left: 40px; font-size: 12px; font-weight: 500'>${time_left}</div>
                <div style='margin-left: 40px; font-size: 11px; color: #888'>${deadline}</div>
            </div>
        `;
    };
    
    this.tag = function(enrollment){
        var color = '';
        color = enrollment.state == 'pending' ? '#aaa' : color;
        color = enrollment.state == 'active' ? '#17d97b' : color;
        color = enrollment.state == 'cutoff' ? '#f56342' : color;
        color = enrollment.state == 'achieved' ? '#36e0cd' : color;
        return `
            <base-tag noticable text-color='#fff' color='${color}'>${enrollment.state}</base-tag>
        `;
    };
    
    this.actions = function(enrollment){
        return `
            <base-button sm upper cta dd left label='View'>
                <cmenu options='${Enrollment.am(enrollment)}'></cmenu>
            </base-button-dd>
        `;
    };
};
