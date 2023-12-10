var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"><b>SC</b>' +
	'<p style="text-align:center; font-size:24px">Please choose your answer below.</p>',
	choices: ['Continue']
  };

  var scale = [
	"Strongly agree",
	"Somewhat agree",
	"A little agree",
	"Neither agree or disagree",
	"A little disagree",
	"Somewhat disagree",
	"Strongly disagree"
  ];

 var questions =[
	{prompt: '<p style="text-align:center; font-size:24px"> I can do just about anything I really set my mind to.</p>',
	name: 'SC1',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> When I really want to do something, I usually find a way to succeed at it.</p>',
	name: 'SC2',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> Whether or not I am able to get what I want is in my own hands.</p>',
	name: 'SC3',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> What happens to me in the future mostly depends on me.</p>',
	name: 'SC4',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> There is little I can do to change many of the important things in my life.</p>',
	name: 'SC5',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> I often feel helpless in dealing with the problems of life.</p>',
	name: 'SC6',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> Other people determine most of what I can and cannot do.</p>',
	name: 'SC7',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> What happens in my life is often beyond my control.</p>',
	name: 'SC8',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> There are many things that interfere with what I want to do.</p>',
	name: 'SC9',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> I have little control over the things that happen to me.</p>',
	name: 'SC10',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> There is really no way I can solve the problems I have.</p>',
	name: 'SC11',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px"> Sometimes I feel I am being pushed around in my life.</p>',
	name: 'SC12',
	labels: scale}
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var SC = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order:false
};
   
var SC_block = {
	timeline: [prompt,SC],
	randomize_order: false,
  };
  

