var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px">We would like to ask you some questions about your emotional life, in particular, how you control (that is, regulate and manage) your emotions.</p>'+
	'<p style="text-align:center; font-size:24px">The questions below involve two distinct aspects of your emotional life.</p>'+
	'<p style="text-align:center; font-size:24px">One is your emotional experience, or what you feel like inside.</p>'+
	'<p style="text-align:center; font-size:24px">The other is your emotional expression, or how you show your emotions in the way you talk, gesture, or behave.</p>'+
	'<p style="text-align:center; font-size:24px">Although some of the following questions may seem similar to one another, they differ in important ways.</p>'+
	'<p style="text-align:center; font-size:24px">For each item, please answer using a 7-point Likert-scale ranging from "Strongly disagree" to "Strongly agree".</p>',

	choices: ['Continue']
};

var scale = [
	"Strongly disagree",
	"Disagree",
	"Slightly disagree",
	"Neutral",
	"Slightly agree",
	"Agree",
	"Strongly agree"
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

	{prompt: '<p style="text-align:center; font-size:24px">I control my emotions by changing the way I think about the situation I am in.</p>',
	name: 'ERQ8',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I am feeling negative emotions, I make sure not to express them.</p>',
	name: 'ERQ9',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I want to feel less negative emotion, I change the way I am thinking about the situation.</p>',
	name: 'ERQ10',
	labels: scale}
];

questions.forEach(function(question) {
    question.required = true;
});

var ERQ = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var ERQ_block = {
	timeline: [prompt, ERQ],
	randomize_order: false
};
