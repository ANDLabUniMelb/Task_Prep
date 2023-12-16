var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"> The next questions are about changes that may be happening to your body.</p>' +
	'<p style="text-align:center; font-size:24px"> These changes normally happen to different young people at different ages.</p>'+
	'<p style="text-align:center; font-size:24px"> For each question, please choose the answer that best describes what is happening to you.</p>',

		choices: ['Continue']
};

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px">Would you say that your growth in height:</p>'+
	'<p style="text-align:center; font-size:24px">("Spurt" means more growth than usual)</p>',
	name: 'SSPDG1',
	labels: [
		"Has not yet begun to spurt",
		"Has barely started",
		"Is definitely underway",
		"Seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Would you say that your body hair growth:</p>'+
    '<p style="text-align:center; font-size:24px">("Body hair" means underarm and pubic hair.)</p>',
	name: 'SSPDG2',
	labels: [
		"Not yet started growing",
		"Has barely started growing",
		"Is definitely underway",
		"Seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have you noticed any skin changes, especially pimples?</p>',
	name: 'SSPDG3',
	labels: [
		"Not yet started showing changes",
    	"Have barely started showing changes",
    	"Skin changes are definitely underway",
    	"Skin changes seem completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have your breasts begun to grow?</p>',
	name: 'SSPDG4',
	labels: [
		"Not yet started growing",
		"Have barely started changing",
    	"Breast growth is definitely started",
    	"Breast growth seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Do you think your development is any earlier or later than most other girls your age?</p>',
	name: 'SSPDG5',
	labels: [
		"Much earlier",
		"Somewhat earlier",
		"About the same",
		"Somewhat later",
		"Much later"
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have you begun to menstruate?</p>',
	name: 'SSPDG6a',
	labels: [
		"Yes (please specify on the next page)",
		"No"
	]},
];

questions.forEach(function(question) {
    question.required = true;
});

var SSPDG = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false,
};

var SSPDG6b = {
	type: 'survey-text',
	questions: [
	{prompt: '<p style="text-align:center; font-size:24px">How old were you when you first menstruated? (Please enter as a number)',
		name: 'SSPDG6b',
		required: true},

	{prompt: '<p style="text-align:center; font-size:24px">Please enter the month as well if you could still recall, otherwise just leave it blank.',
	name: 'SSPDG6bb'},
],
};

// Extra questions for SSPDG6a
var conditionalSSPDG6b = {
	timeline: [SSPDG6b],
	conditional_function: function() {
	  // Last answer from SSPDG (Yes = 0, No = 1)
	  var lastResponse = jsPsych.data.get().filter({trial_type: 'survey-likert'}).last(1).values()[0].responses;
	  var menstruationResponse = JSON.parse(lastResponse)['SSPDG6a'];
  
	  // If Yes
	  if (menstruationResponse === 0) {
		return true; // Showing SSPDG6b
	  } else {
		return false; // Not showing SSPDG6b
	  }
	},
	loop_function: function(data){
	var lastTrialData = JSON.parse(jsPsych.data.getLastTrialData().select('responses').values);
	var SSPDG6b = lastTrialData.SSPDG6b;
	console.log(jsPsych.data.getLastTrialData().select('responses').values);
	console.log(SSPDG6b);
	if (isNaN(SSPDG6b)) {
            alert("Please enter the age at which you first menstruated as a number (make sure to remove any spaces).");
            return true;}
	return false;
	}
	
  };

var SSPDG_block = {
	timeline: [prompt, SSPDG, conditionalSSPDG6b],
	randomize_order: false,
	}