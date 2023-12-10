var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"><b>SSPDG</b>' +
	'<p style="text-align:center; font-size:24px"> The next questions are about changes that may be happening to your body.</p>' +
		'<p style="text-align:center; font-size:24px"> These changes normally happen to different young people at different ages.</p>',
		choices: ['Continue']
};

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px">Would you say that your growth in height:</p>'+
	'<p style="text-align:center; font-size:24px">("Spurt" means more growth than usual)</p>',
	name: 'SDPPG1',
	labels: [
		"Has not yet begun to spurt",
		"Has barely started",
		"Is definitely underway",
		"Seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Would you say that your body hair growth:</p>'+
    '<p style="text-align:center; font-size:24px">("Body hair" means hair any place other than your head, such as under your arms.)</p>',
	name: 'SDPPG2',
	labels: [
		"Not yet started growing",
		"Has barely started growing",
		"Is definitely underway",
		"Seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have you noticed any skin changes, especially pimples?</p>',
	name: 'SDPPG3',
	labels: [
		"Not yet started showing changes",
    	"Have barely started showing changes",
    	"Skin changes are definitely underway",
    	"Skin changes seem completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have your breasts have begun to grow?</p>',
	name: 'SDPPG4',
	labels: [
		"Not yet started growing",
		"Have barely started changing",
    	"Breast growth is definitely started",
    	"Breast growth seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Do you think your development is any earlier or later than most other girls your age?</p>',
	name: 'SDPPG5',
	labels: [
		"Much earlier",
		"Somewhat earlier",
		"About the same",
		"Somewhat later",
		"Much later"
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have you begun to menstruate?</p>',
	name: 'SDPPG6a',
	labels: [
		"Yes (please specify on the next page)",
		"No"
	]},
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var SSPDG = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false,
};

var SDPPG6b = {
	type: 'survey-text',
	questions: [
	{prompt: '<p style="text-align:center; font-size:24px">How old were you when you first menstruated? (Please enter as a number)',
		name: 'SDPPG6b',
		required: true},

	{prompt: '<p style="text-align:center; font-size:24px">Please enter the month as well if you could still recall, otherwise just leave it blank.',
	name: 'SDPPG6bb'},
],
};

// Extra questions for SSPDG6a
var conditionalSDPPG6b = {
	timeline: [SDPPG6b],
	conditional_function: function() {
	  // Last answer from SSPDG (Yes = 0, No = 1)
	  var lastResponse = jsPsych.data.get().filter({trial_type: 'survey-likert'}).last(1).values()[0].responses;
	  var menstruationResponse = JSON.parse(lastResponse)['SDPPG6a'];
  
	  // If Yes
	  if (menstruationResponse === 0) {
		return true; // Showing SDPPG6b
	  } else {
		return false; // Not showing SDPPG6b
	  }
	},
	loop_function: function(data){
	var lastTrialData = JSON.parse(jsPsych.data.getLastTrialData().select('responses').values);
	var SDPPG6b = lastTrialData.SDPPG6b;
	console.log(jsPsych.data.getLastTrialData().select('responses').values);
	console.log(SDPPG6b);
	if (isNaN(SDPPG6b)) {
            alert("Please enter the age at which you first menstruated as a number (make sure to remove any spaces).");
            return true;}
	return false;
	}
	
  };

var SSPDG_block = {
	timeline: [prompt, SSPDG, conditionalSDPPG6b],
	randomize_order: false,
	}