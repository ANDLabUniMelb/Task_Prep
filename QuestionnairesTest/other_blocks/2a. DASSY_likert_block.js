var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"><b>DASSY</b>' +
		'<p style="text-align:center; font-size:24px"> We would like to find out how you have been feeling <b>in the past week</b>.</p>' +
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
	name: 'DASS1',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I felt dizzy, like I was about to faint.</p>',
	name: 'DASS2',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I did not enjoy anything.</p>',
	name: 'DASS3',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I had trouble breathing (e.g. fast breathing), even though I wasn\'t exercising and I was not sick.</p>',
	name: 'DASS4',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I hated my life.</p>',
	name: 'DASS5',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I found myself over-reacting to situations.</p>',
	name: 'DASS6',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">My hands felt shaky.</p>',
	name: 'DASS7',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I was stressing about lots of things.</p>',
	name: 'DASS8',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I felt terrified.</p>',
	name: 'DASS9',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">There was nothing nice I could look forward to.</p>',
	name: 'DASS10',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I was easily irritated.</p>',
	name: 'DASS11',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I found it difficult to relax.</p>',
	name: 'DASS12',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I could not stop feeling sad.</p>',
	name: 'DASS13',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I got annoyed when people interrupted me.</p>',
	name: 'DASS14',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I felt like I was about to panic.</p>',
	name: 'DASS15',
	labels: scale },

	{prompt: '<p style="text-align:center; font-size:24px">I hated myself.</p>',
	name: 'DASS16',
	labels: scale }
	];

// questions.forEach(function(question) {
//     question.required = true;
// });

var DASSY = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var DASSY_block = {
	timeline: [prompt, DASSY],
	randomize_order: false
};
