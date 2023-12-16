var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px">Please select the answer that best corresponds to how much you agree with each item.</p>',
	choices: ['Continue']
};

var scale = [
	"Not at all characteristic of me",
	"A little characteristic of me",
	"Somewhat characteristic of me",
	"Very characteristic of me",
	"Entirely characteristic of me"
];

var questions = [
		{prompt: '<p style="text-align:center; font-size:24px">Unforeseen events upset me greatly.</p>',
		name: 'IU1',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">It frustrates me not having all the information I need.</p>',
		name: 'IU2',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">Uncertainty keeps me from living a full life.</p>',
		name: 'IU3',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">One should always look ahead so as to avoid surprises.</p>',
		name: 'IU4',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">A small unforeseen event can spoil everything, even with the best of planning.</p>',
		name: 'IU5',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">When it\'s time to act, uncertainty paralyses me.</p>',
		name: 'IU6',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">When I am uncertain I can\'t function very well.</p>',
		name: 'IU7',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I always want to know what the future has in store for me.</p>',
		name: 'IU8',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I can\'t stand being taken by surprise.</p>',
		name: 'IU9',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">The smallest doubt can stop me from acting.</p>',
		name: 'IU10',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I should be able to organize everything in advance.</p>',
		name: 'IU11',
		labels: scale},

		{prompt: '<p style="text-align:center; font-size:24px">I must get away from all uncertain situations.</p>',
		name: 'IU12',
		labels: scale}
];

questions.forEach(function(question) {
    question.required = true;
});

var IU = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var IU_block = {
	timeline: [prompt, IU],
	randomize_order: false
};