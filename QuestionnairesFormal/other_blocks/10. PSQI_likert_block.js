var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"> The following questions relate to your usual sleep habits <b>during the past month only</b>.</p>' +
		'<p style="text-align:center; font-size:24px"> Your answers should indicate the most accurate reply for the majority of days and nights in the past month.</p>',
		choices: ['Continue']
};

var questions1 = [
    {prompt: '<p style="text-align:center; font-size:24px"><br>During the past month, when have you usually gone to bed at night?' +
    '<p style="text-align:center; font-size:24px"> (HHMM, 24 hour time. For example, 10pm is 2200.)'},

    {prompt: '<p style="text-align:center; font-size:24px">During the past month, how long has it usually take you to fall asleep each night? (In minutes)'},

    {prompt: '<p style="text-align:center; font-size:24px">During the past month, when have you usually gotten up in the morning?'+
    '<p style="text-align:center; font-size:24px">(HHMM, 24 hour time. For example, 9am is 0900.)'},

    {prompt: '<p style="text-align:center; font-size:24px">During the past month, how many hours of actual sleep did you get at night?' +
	'<p style="text-align:center; font-size:24px">(This may be different than the number of hours you spend in bed.)'},
];

questions1.forEach(function(question) {
    question.required = true;
});

var part1 = {
    type: 'survey-text',
    preamble: ['<p style="text-align:center; font-size:24px"><br><b>Please enter numbers only for the following questions:</b>'],
    questions: questions1,
};

var PSQI1 = {
    timeline: [part1],
    loop_function: function(data){
        var lastTrialData = JSON.parse(jsPsych.data.getLastTrialData().select('responses').values);
        var bedtime = lastTrialData.Q0;
        var asleep = lastTrialData.Q1;
        var getup = lastTrialData.Q2;
        var sleep = lastTrialData.Q3;
        console.log(jsPsych.data.getLastTrialData().select('responses').values);
        console.log(bedtime, asleep, getup, sleep);
        if (bedtime == '' || asleep == '' || getup == '' || sleep == '') {
            alert("Please make sure you answer all questions.");
            return true;
        }
        if (isNaN(bedtime) || bedtime.length != 4) {
            alert("Please enter your bed time in the format of HHMM (make sure to remove any spaces).");
            return true;
        }
        if (isNaN(asleep)) {
            alert("Please enter the time you take to fall asleep as a number (make sure to remove any spaces)");
            return true;
        }
        if (isNaN(getup) || getup.length != 4) {
            alert("Please enter the time you get up in the format of HHMM (make sure to remove any spaces).");
            return true;
        }
        if (isNaN(sleep)) {
            alert("Please enter your actual sleep time as a number (make sure to remove any spaces).");
            return true;
        }
        return false;
    }
}

var scale = [
    "Not during the past month",
    "Less than once a week",
    "Once or twice a week",
    "Three or more times a week"
]

var questions2 = [
    {prompt: '<p style="text-align:center; font-size:24px"><b>During the past month, how often have you had trouble sleeping because you...</b></p><br>' +
    '<p style="text-align:center; font-size:24px">Cannot get to sleep within 30 minutes.',
    name: "PSQI1",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Wake up in the middle of the night or early morning',
    name: "PSQI2",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Have to get up to use the bathroom',
    name: "PSQI3",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Cannot breathe comfortably',
    name: "PSQI4",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Cough or snore loudly',
    name: "PSQI5",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Feel too cold',
    name: "PSQI6",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Feel too hot',
    name: "PSQI7",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Had bad dreams',
    name: "PSQI8",
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Have pain',
    name: "PSQI9",
    labels: scale},
];

questions2.forEach(function(question) {
    question.required = true;
});

var PSQI2 = {
	type: 'survey-likert',
	questions: questions2,
	randomize_question_order: false
};


var questions3 = [
    {prompt: '<p style="text-align:center; font-size:24px">During the past month, how would you rate your sleep quality overall?',
    name: "PSQI10",
    labels: [
        "Very good",
        "Fairly good",
        "Fairly bad",
        "Very bad"
    ],
    randomize_option_order: false},

    {prompt: '<p style="text-align:center; font-size:24px">During the past month, how often have you taken medicine (prescribed or "over the counter") to help you sleep?',
    name: "PSQI11",
    labels: [
    "Not during the past month",
    "Less than once a week",
    "Once or twice a week",
    "Three or more times a week"
    ],
    randomize_option_order: false},

    {prompt: '<p style="text-align:center; font-size:24px">During the past month, how often have you had trouble staying awake while driving, eating meals, or engaging in social activity?',
    name: "PSQI12",
    labels: [
    "Not during the past month",
    "Less than once a week",
    "Once or twice a week",
    "Three or more times a week"
    ],
    randomize_option_order: false},

    {prompt: '<p style="text-align:center; font-size:24px">During the past month, how much of a problem has it been for you to keep up enough enthusiasm to get things done?',
    name: "PSQI13",
    labels: [
    "No problem at all",
    "Only a very slight problem",
    "Somewhat of a problem",
    "A very big problem"
    ],
    randomize_option_order: false},

    {prompt: '<p style="text-align:center; font-size:24px">Do you have a bed partner or roommate?',
    name: "PSQI14",
    labels: [
    "No bed partner or roommate",
    "Partner/roommate in other room",
    "Partner in same room, but not same bed",
    "Partner in same bed"
    ],
    randomize_option_order: false},
];

questions3.forEach(function(question) {
    question.required = true;
});

var PSQI3 = {
	type: 'survey-likert',
	questions: questions3,
	randomize_question_order: false
};


var	questions4 = [
	{prompt: '<p style="text-align:center; font-size:24px"><b>If you have a roommate or bed partner, ask him/her how often in the past month you have had...</b></p><br>'+
    '<p style="text-align:center; font-size:24px">Loud snoring',
		name: 'PSQIOptional1',
        labels: scale},
    
    {prompt: '<p style="text-align:center; font-size:24px">Long pauses between breaths while asleep',
		name: 'PSQIOptional2',
        labels: scale},
    
   {prompt: '<p style="text-align:center; font-size:24px">Legs twitching or jerking while you sleep',
	name: 'PSQIOptional3',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Episodes of disorientation or confusion during sleep',
	name: 'PSQIOptional4',
    labels: scale},
];


questions4.forEach(function(question) {
    question.required = true;
});

var part4 = {
	type: 'survey-likert',
    questions: questions4,
    randomize_question_order: false
};


var PSQIOptional = {
	timeline: [part4],
	conditional_function: function() {
	  var lastResponse = jsPsych.data.get().filter({trial_type: 'survey-likert'}).last(1).values()[0].responses;
	  var menstruationResponse = JSON.parse(lastResponse)['PSQI14'];
	  if (menstruationResponse === 1 ||menstruationResponse === 2 || menstruationResponse === 3) {
		return true;
	  } else {
		return false;
	  }
	}
  };


var PSQI_block = {
	timeline: [prompt, PSQI1, PSQI2, PSQI3, PSQIOptional],
    randomize_order: false,
}

