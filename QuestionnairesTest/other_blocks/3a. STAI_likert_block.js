var prompt = {
	type: 'html-button-response',
	stimulus:'<p style="text-align:center; font-size:24px"><b>STAI</b>' +
	'<p style="text-align:center; font-size:24px">A number of statements which people have used to describe themselves are given below.</p>' +
	'<p style="text-align:center; font-size:24px">Read each statement and choose an answer to indicate how you <b> generally </b> feel.</p>' +
	'<p style="text-align:center; font-size:24px">There are no right or wrong answers.</p>' + 
	'<p style="text-align:center; font-size:24px">Do not spend too much time on any one statement. </p>',
	choices: ['Continue'] 
};

var scale = [
	"Almost never",
	"Sometimes",
	"Often",
	"Almost always"
];

var questions = [
		{prompt: '<p style="text-align:center; font-size:24px"><b>Generally...</b>'+
		'<p style="text-align:center; font-size:24px"><br>I feel pleasant.',
		name: 'STAIT1', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel nervous and restless.',
		name: 'STAIT2', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel satisfied with myself.',
		name: 'STAIT3', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I wish I could be as happy as others seem to be.',
		name: 'STAIT4', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel like a failure.',
		name: 'STAIT5', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel rested.',
		name: 'STAIT6', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I am "calm, cool, and collected".',
		name: 'STAIT7', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I feel that difficulties are piling up so that I cannot overcome them.',
		name: 'STAIT8', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I worry too much over something that really doesn\'t matter.',
		name: 'STAIT9', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I am happy.',
		name: 'STAIT10', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I have disturbing thoughts.',
		name: 'STAIT11', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I lack self-confidence.',
		name: 'STAIT12', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel secure.',
		name: 'STAIT13', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I make decisions easily.',
		name: 'STAIT14', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel inadequate.',
		name: 'STAIT15', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I am content.',
		name: 'STAIT16', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">Some unimportant thought runs through my mind and bothers me.',
		name: 'STAIT17', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I take disappointments so keenly that I can\'t put them out of my mind.',
		name: 'STAIT18', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I am a steady person.',
		name: 'STAIT19', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I get in a state of tension or turmoil as I think over my recent concerns and interests.',
		name: 'STAIT20', 
		labels: scale}
		
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var STAI = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order:false
};

var STAI_block = {
	timeline: [prompt, STAI],
	randomize_order: false,
};

