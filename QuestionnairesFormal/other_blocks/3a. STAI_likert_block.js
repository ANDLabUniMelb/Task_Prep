var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px">A number of statements which people have used to describe themselves are given below.</p>' +
	'<p style="text-align:center; font-size:24px">Read each statement and choose an answer to indicate how you <b> generally </b> feel.</p>' +
	'<p style="text-align:center; font-size:24px">There are no right or wrong answers.</p>' + 
	'<p style="text-align:center; font-size:24px">Do not spend too much time on any one statement, but give the answer which seems to describe how you generally feel.</p>',
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
		name: 'STAI1', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel nervous and restless.',
		name: 'STAI2', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel satisfied with myself.',
		name: 'STAI3', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I wish I could be as happy as others seem to be.',
		name: 'STAI4', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel like a failure.',
		name: 'STAI5', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel rested.',
		name: 'STAI6', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I am "calm, cool, and collected".',
		name: 'STAI7', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I feel that difficulties are piling up so that I cannot overcome them.',
		name: 'STAI8', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I worry too much over something that really doesn\'t matter.',
		name: 'STAI9', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I am happy.',
		name: 'STAI10', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I have disturbing thoughts.',
		name: 'STAI11', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I lack self-confidence.',
		name: 'STAI12', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel secure.',
		name: 'STAI13', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I make decisions easily.',
		name: 'STAI14', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I feel inadequate.',
		name: 'STAI15', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I am content.',
		name: 'STAI16', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">Some unimportant thought runs through my mind and bothers me.',
		name: 'STAI17', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I take disappointments so keenly that I can\'t put them out of my mind.',
		name: 'STAI18', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I am a steady person.',
		name: 'STAI19', 
		labels: scale},
	
		{prompt: '<p style="text-align:center; font-size:24px">I get in a state of tension or turmoil as I think over my recent concerns and interests.',
		name: 'STAI20', 
		labels: scale}
		
];

questions.forEach(function(question) {
    question.required = true;
});

var STAI = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order:false
};

var STAI_block = {
	timeline: [prompt, STAI],
	randomize_order: false,
};

