var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"> We would like to find out how you have been feeling <b>in the past week</b>.</p>' +
		'<p style="text-align:center; font-size:24px"> There are some sentences below.</p>' +
		'<p style="text-align:center; font-size:24px"> Please select the statement which best shows how true each sentence was of you during the past week.</p>' +
		'<p style="text-align:center; font-size:24px"> There are no right or wrong answers. </p>',
		choices: ['Continue']
};

var scale = [
	"Not true",
	"A little true",
	"Fairly true",
	"Very true"
];

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px"><b>In the past week...</b></p><br>'+
	'<p style="text-align:center; font-size:24px">I got upset about little things.</p>',
	name: 'DASSY1',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I felt dizzy, like I was about to faint.</p>',
	name: 'DASSY2',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I did not enjoy anything.</p>',
	name: 'DASSY3',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I had trouble breathing (e.g. fast breathing), even though I wasn\'t exercising and I was not sick.</p>',
	name: 'DASSY4',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I hated my life.</p>',
	name: 'DASSY5',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I found myself over-reacting to situations.</p>',
	name: 'DASSY6',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">My hands felt shaky.</p>',
	name: 'DASSY7',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I was stressing about lots of things.</p>',
	name: 'DASSY8',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I felt terrified.</p>',
	name: 'DASSY9',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">There was nothing nice I could look forward to.</p>',
	name: 'DASSY10',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I was easily irritated.</p>',
	name: 'DASSY11',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I found it difficult to relax.</p>',
	name: 'DASSY12',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I could not stop feeling sad.</p>',
	name: 'DASSY13',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I got annoyed when people interrupted me.</p>',
	name: 'DASSY14',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I felt like I was about to panic.</p>',
	name: 'DASSY15',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I hated myself.</p>',
	name: 'DASSY16',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I felt like I was no good.</p>',
	name: 'DASSY17',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I was easily annoyed.</p>',
	name: 'DASSY18',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I could feel my heart beating really fast, even though I had\'t done any hard exercise.</p>',
	name: 'DASSY19',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I felt scared for no good reason.</p>',
	name: 'DASSY20',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I felt that life was terrible.</p>',
	name: 'DASSY21',
	labels: scale}
	];

questions.forEach(function(question) {
    question.required = true;
});

var DASSY = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var DASSY_block = {
	timeline: [prompt, DASSY],
	randomize_order: false
};
