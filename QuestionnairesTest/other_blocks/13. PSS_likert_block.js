var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"><b>PSS</b>' +
	'<p style="text-align:center; font-size:24px">The questions in this scale ask about your feelings and thoughts.' +
		'<p style="text-align:center; font-size:24px"> Please indicate how often you felt or thought a certain way <b> during the last month</b>.</p>',
		choices: ['Continue']
};

var scale = [
	"Never",
	"Almost never",
	"Sometimes",
	"Fairly often",
	"Very often"
];

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px"><b>In the last month...</b></p><br>'+
	'<p style="text-align:center; font-size:24px">How often have you been upset because of something that happened unexpectedly?',
	name: 'PSS1',
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you felt that  you were unable to control the important things in your life?',
	name: 'PSS2', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you felt nervous and stressed?',
	name: 'PSS3', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you felt confident about your ability to handle your personal problems?',
	name: 'PSS4', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you felt that things were going your way?',
	name: 'PSS5', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you found that you could not cope with all the things that you had to do?',
	name: 'PSS6', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you been able to control irritations in your life?',
	name: 'PSS7', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you felt that you were on top of things?',
	name: 'PSS8', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you been angered because of things that were outside of your control?',
	name: 'PSS9', 
	labels: scale},
	
	{prompt: '<p style="text-align:center; font-size:24px">How often have you felt difficulties were piling up so high that you could not overcome them?',
	name: 'PSS10', 
	labels: scale}
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var PSS = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order:false
};

var PSS_block = {
	timeline: [prompt, PSS],
	randomize_order: false,
};

