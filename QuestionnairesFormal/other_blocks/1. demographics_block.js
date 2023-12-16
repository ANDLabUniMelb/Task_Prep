var staticAge = '';
var staticSex = '';


var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"> In the following pages, please provide us with some basic information about yourself.</p>',
		choices: ['Continue']
};

// Text p1
var demographics1 = {
    type: 'survey-text',
    name: "name",
    questions:[
        {prompt: '<p style="text-align:center; font-size:24px"><br>What is your name? (First, Last)', required: true}
]};


// Text p2
var questions2 = [
    {prompt: '<p style="text-align:center; font-size:24px"><br>How old are you?'},
    {prompt: '<p style="text-align:center; font-size:24px">What is your date of birth? (YYYYMMDD)'},
    {prompt: '<p style="text-align:center; font-size:24px">What is your current height? (cm)'},
    {prompt: '<p style="text-align:center; font-size:24px">What is your current weight? (kg)'},
    {prompt: '<p style="text-align:center; font-size:24px">How many hours do you exercise per week?'},
];

questions2.forEach(function(question) {
    question.required = true;
});

var part2 = {
    type: 'survey-text',
    preamble: ['<p style="text-align:center; font-size:24px"><b>Please enter numbers only for the following questions:</b>'],
    questions: questions2,
};

    // Ensure only numbers were entered
var demographics2 = {
    timeline: [part2],
    loop_function: function(data){
        var lastTrialData = JSON.parse(jsPsych.data.getLastTrialData().select('responses').values);
        var age = lastTrialData.Q0;
        staticAge = age;
        console.log('Age' + staticAge);
        var birthday = lastTrialData.Q1;
        var height = lastTrialData.Q2;
        var weight = lastTrialData.Q3;
        var exercise = lastTrialData.Q4;
        console.log(jsPsych.data.getLastTrialData().select('responses').values);
        console.log(age,weight,height,birthday,exercise);
        if (age == '' || birthday == '' || height == '' || weight == '' || exercise == '') {
            alert("Please make sure you answer all questions.");
            return true;
        }
        if (isNaN(age)) {
            alert("Please enter your age as a number (make sure to remove any spaces).");
            return true;
        }
        if (isNaN(birthday) || birthday.length != 8) {
            alert("Please enter your date of birth in the format of YYYYMMDD (make sure to remove any spaces).");
            return true;
        }
        if (isNaN(height)) {
            alert("Please enter your height as a number (make sure to remove any spaces).");
            return true;
        }
        if (isNaN(weight)) {
            alert("Please enter your weight as a number (make sure to remove any spaces).");
            return true;
        }
        if (isNaN(exercise)) {
            alert("Please enter the exercise hours as a number (make sure to remove any spaces).");
            return true;
        }
        return false;
    }
}

// Drop-down box
var demographics3 = {
    type: 'survey-select',
    questions: [
        {prompt: '<p style="text-align:center; font-size:24px">What is your current gender identity?',
        name: 'Gender',
        placeholder: ' ',
        options: [
            'Woman',
            'Man',
            'Trans Male/Trans Man',
            'Trans Female/Trans Woman',
            'Genderqueer/Gender non-conforming',
            'Different Identity',
            'Prefer not to say'
        ],
        randomize_option_order: false},

        {prompt: '<p style="text-align:center; font-size:24px">What sex were you assigned at birth (on your original birth certificate)?',
        name: 'Sex',
        placeholder: ' ',
        options: ['Male', 'Female'],
        randomize_option_order: false},

        {prompt: '<p style="text-align:center; font-size:24px">What is your dominant hand?',
        name: 'Hand',
        placeholder: ' ',
        options: ['Left', 'Right'],
        randomize_option_order: false},

        {prompt: '<p style="text-align:center; font-size:24px">Please indicate the highest level of education you have completed.',
        name: 'Education',
        placeholder: ' ',
        options: [
            'Still at secondary school',
            'Did not finish secondary school',
            'Year 12 or equivalent',
            'Certificate level, diploma, or advanced diploma',
            'Bachelor\'s degree',
            'Postgraduate degree (e.g. Honours, Masters, Doctorate, PhD)'
        ],
        randomize_option_order: false},

        {prompt: '<p style="text-align:center; font-size:24px">How would you describe your main racial/ethnic background?',
        name: 'Ethnicity',
        placeholder: ' ',
        options: [
            'Australian - neither Aboriginal nor Torres Strait Islander',
            'Australian - Aboriginal or Torres Strait Islander',
            'Pacific Islander, or other Oceania',
            'British or European',
            'Asian',
            'Middle Eastern',
            'African',
            'North American',
            'Central or Southern American'
        ],
        randomize_option_order: false},

        {prompt: '<p style="text-align:center; font-size:24px">What\'s the main language you spoke at home?',
        name: 'Language',
        placeholder: ' ',
        options: [
            'English',
            'Other (please specify on the next page)'
        ],
        randomize_option_order: false},

        {prompt: '<p style="text-align:center; font-size:24px">Are you currently in paid employment? ',
        name: 'Employment',
        placeholder: ' ',
        options: [
            'Yes (please specify on the next page)',
            'No'
        ],
        randomize_option_order: false},

        {prompt: '<p style="text-align:center; font-size:24px">Are you currently taking any medications? ',
        name: 'Medication',
        placeholder: ' ',
        options: [
            'Yes (please specify on the next page)',
            'No'
        ],
        randomize_option_order: false},
        
        
],

    // Extra questions for 'Language', 'Employment', and 'Medication'
on_finish: function(data){
    // Extract responses
    var responses = JSON.parse(data.responses);
    conditionalQuestions = [];
    staticSex = responses.Sex;

        // Language
    if(responses.Language === 'Other (please specify on the next page)'){
        conditionalQuestions.push({
            prompt: 'What\'s the main language you spoke at home?',
            name: 'LanguageOptional',
            required: true
        });
    }

        // Employment
    if(responses.Employment === 'Yes (please specify on the next page)'){
        conditionalQuestions.push({
            prompt: 'How many hours do you work per week? (Please enter as a number)',
            name: 'EmploymentOptional',
            required: true
        });
    }

        // Medication
    if(responses.Medication === 'Yes (please specify on the next page)'){
        conditionalQuestions.push({
            prompt: 'What medications are you taking?',
            name: 'MedicationOptional',
            required: true
        });
        
    }
    conditionalBlock.questions = conditionalQuestions;

    var age = staticAge;
    var sex = staticSex;
    // var pavlovia_finish = {
    //     type: "pavlovia",
    //     command: "finish"
    //   };
      

    newTimeline = [];

    if (age >= 18) {

        newTimeline = [
            DASS21_block, //2b adults
            STAI_block, //3a adults
            IU_block, //4
            BISBAS_block, //5
            AFML_block, //6
            ERQ_block, //7
            DERS_block, //8
            SCAARED_block, //9b adults
            PSQI_block, //10
            PANASSF_block, //11
            PTQ_block, //12
            PSS_block, //13
            SC_block, //14
            GSE_block, //15
        ];

    } else {
        newTimeline = [
            DASSY_block, //2a adolescents
            STAIY_block, //3b adolescents
            IU_block, //4
            BISBAS_block, //5
            AFML_block, //6
            ERQ_block, //7
            DERS_block, //8
            SCARED_block, //9a adolescents
            PSQI_block, //10
            PANASSF_block, //11
            PTQ_block, //12
            PSS_block, //13
            SC_block, //14
            GSE_block, //15
        ]
        if (sex === 'Female') {
            newTimeline.push(SSPDG_block); // 16b girls
    
        } else {
            newTimeline.push(SSPDB_block); // 16a boys
        }
    }
    // newTimeline.push(pavlovia_finish);
    newTimeline.push(completion_block);
    jsPsych.addNodeToEndOfTimeline({timeline: newTimeline});
       
}
};

var preConditionalBlock = {
    type: 'survey-text',
    questions: function() {return conditionalQuestions;}

}

var conditionalBlock = {
    timeline: [preConditionalBlock],
    conditional_function: function() {

        return conditionalQuestions.length > 0;
    },
    loop_function: function(data){
        var lastTrialData = JSON.parse(jsPsych.data.getLastTrialData().select('responses').values);
        console.log(lastTrialData);
        var EmploymentOptional = lastTrialData.EmploymentOptional;
        if (EmploymentOptional != undefined) {
            if (isNaN(EmploymentOptional)) {
                alert("Please enter the working hours as a number (make sure to remove any spaces).");
                return true;}
        }
        return false;
        }
};



var demographics_block = {
	timeline: [prompt, demographics1, demographics2, demographics3, conditionalBlock],
    randomize_order: false,
    // on_finish: function(data){
        

    //     // update timeline
    //     // jsPsych.addNodeToEndOfTimeline({ timeline: newTimeline });
    // }
}