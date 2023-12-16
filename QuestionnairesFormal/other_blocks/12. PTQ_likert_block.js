var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px">In this questionnaire, you will be asked to describe how you <b>typically</b> think about negative experiences or problems.' +
		'<p style="text-align:center; font-size:24px">Please read the following statements and rate the extent to which they apply to you when you think about negative experiences or problems.</p>',
		choices: ['Continue']
};

var scale = [
	"Never",
	"Rarely",
	"Sometimes",
	"Often",
	"Almost always"
];

var questions = [
		{prompt: '<p style="text-align:center; font-size:24px"><b>Typically...</b></p><br>' +
		'<p style="text-align:center; font-size:24px">The same thoughts keep going through my mind again and again.',
		name: 'PTQ1',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">Thoughts intrude into my mind.',
		name: 'PTQ2',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I can\'t stop dwelling on them.',
		name: 'PTQ3',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I think about many problems without solving any of them.',
		name: 'PTQ4', labels: scale},
		{prompt: '<p style="text-align:center; font-size:24px">I can\'t do anything else while thinking about my problems.',
		name: 'PTQ5',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">My thoughts repeat themselves.',
		name: 'PTQ6',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">Thoughts come to my mind without me wanting them to.',
		name: 'PTQ7',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I get stuck on certain issues and can\'t move on.',
		name: 'PTQ8',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I keep asking myself questions without finding an answer.',
		name: 'PTQ9',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">My thoughts prevent me from focusing on other things.',
		name: 'PTQ10',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I keep thinking about the same issue all the time.',
		name: 'PTQ11', 
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">Thoughts just pop into my mind.',
		name: 'PTQ12',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I feel driven to continue dwelling on the same issue.',
		name: 'PTQ13',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">My thoughts are not much help to me.',
		name: 'PTQ14',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">My thoughts take up all my attention.',
		name: 'PTQ15',
		labels: scale}
	];

questions.forEach(function(question) {
    question.required = true;
});

var PTQ = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var PTQ_block = {
	timeline: [prompt, PTQ],
	randomize_order: false
};