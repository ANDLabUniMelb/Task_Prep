var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"><b>SSPDB</b>' +
	'<p style="text-align:center; font-size:24px"> The next questions are about changes that may be happening to your body.</p>' +
		'<p style="text-align:center; font-size:24px"> These changes normally happen to different young people at different ages.</p>',
		choices: ['Continue']
};

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px">Would you say that your growth in height:</p>'+
	'<p style="text-align:center; font-size:24px">("Spurt" means more growth than usual)</p>',
	name: 'SDPPB1',
	labels: [
		"Has not yet begun to spurt",
		"Has barely started",
		"Is definitely underway",
		"Seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Would you say that your body hair growth:</p>'+
    '<p style="text-align:center; font-size:24px">("Body hair" means hair any place other than your head, such as under your arms.)</p>',
	name: 'SDPPB2',
	labels: [
		"Not yet started growing",
		"Has barely started growing",
		"Is definitely underway",
		"Seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have you noticed any skin changes, especially pimples?</p>',
	name: 'SDPPB3',
	labels: [
		"Not yet started showing changes",
    	"Have barely started showing changes",
    	"Skin changes are definitely underway",
    	"Skin changes seem completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have you noticed a deepening of your voice?</p>',
	name: 'SDPPB4',
	labels: [
		"Not yet started showing changes",
    	"Have barely started changing",
    	"Voice change is definitely underway",
    	"Voice change seems completed",
	]},

	{prompt: '<p style="text-align:center; font-size:24px">Have you begun to grow hair on your face?</p>',
	name: 'SDPPB5',
	labels: [
		"Not yet started growing hair",
    	"Has barely started growing hair",
    	"Facial hair growth is definitely underway",
    	"Facial hair growth seems completed",
	]},
	{prompt: '<p style="text-align:center; font-size:24px">Do you think your development is any earlier or later than most other boys your age?</p>',
	name: 'SDPPG6',
	labels: [
		"Much earlier",
		"Somewhat earlier",
		"About the same",
		"Somewhat later",
		"Much later"
	]},
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var SSPDB = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var SSPDB_block = {
	timeline: [prompt, SSPDB],
	randomize_order: false
};