var prompt = {
	type: 'html-button-response',
	stimulus:'<p style="text-align:center; font-size:24px"><b>ERQ</b>' +
	'<p style="text-align:center; font-size:24px">For each item, indicate how much you agree or disagree by clicking your response.</p>',
	choices: ['Continue']
};

var scale = [
	"Strongly Disagree",
	"Disagree",
	"Slightly Disagree",
	"Neutral",
	"Slightly Agree",
	"Agree",
	"Strongly Agree"
];

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px">When I want to feel more positive emotion (such as joy or amusement), I change what I am thinking about.</p>',
	name: 'ERQ1',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I keep my emotions to myself.</p>',
	name: 'ERQ2',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I want to feel less negative emotion (such as sadness or anger), I change what I am thinking about.</p>',
	name: 'ERQ3',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I am feeling positive emotions, I am careful not to express them.</p>',
	name: 'ERQ4',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I am faced with a stressful situation, I make myself think about it in a way that helps me stay calm.</p>',
	name: 'ERQ5',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I control my emotions by not expressing them.</p>',
	name: 'ERQ6',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I want to feel more positive emotion, I change the way I am thinking about the situation.</p>',
	name: 'ERQ7',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I control my emotions by changing the way I think about the situation Iam in.</p>',
	name: 'ERQ8',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I am feeling negative emotions, I make sure not to express them.</p>',
	name: 'ERQ9',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I want to feel less negative emotion, I change the way I am thinking about the situation.</p>',
	name: 'ERQ10',
	labels: scale}
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var ERQ = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var ERQ_block = {
	timeline: [prompt, ERQ],
	randomize_order: false
};
