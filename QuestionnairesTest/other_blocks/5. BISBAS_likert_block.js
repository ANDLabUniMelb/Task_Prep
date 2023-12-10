var prompt = {
	type: 'html-button-response',
	stimulus:'<p style="text-align:center; font-size:24px"><b>BISBAS</b>' +
	'<p style="text-align:center; font-size:24px"> The following are statements that a person may either agree with or disagree with.</p>' +
		'<p style="text-align:center; font-size:24px">For each item, indicate how much you agree or disagree with what the item says. </p>' +
		'<p style="text-align:center; font-size:24px">Please be as accurate and honest as you can be. </p>' +
		'<p style="text-align:center; font-size:24px">Do not worry about being "consistent" in your responses. </p>',
		choices: ['Continue']
};

var scale = [
	"Very false for me",
	"Somewhat false for me",
	"Somewhat true for me",
	"Very true for me",
];

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px">A person\'s family is the most important thing in life.',
	name: 'BISBAS1', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Even if something bad is about to happen to me, I rarely experience fear or nervousness.',
	name: 'BISBAS2', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I go out of my way to get things I want.',
	name: 'BISBAS3', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I\'m doing well at something, I love to keep at it.',
	name: 'BISBAS4', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I am always willing to try something new if I think it will be fun.',
	name: 'BISBAS5', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">How I dress is important to me.',
	name: 'BISBAS6', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I get something I want, I feel excited and energized.',
	name: 'BISBAS7', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Criticism or scolding hurts me quite a bit.',
	name: 'BISBAS8', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I want something, I usually go all-out to get it.',
	name: 'BISBAS9', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I will often do things for no other reason than that they might be fun.',
	name: 'BISBAS10', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">It\'s hard for me to find the time to do things such as get a haircut.',
	name: 'BISBAS11', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">If I see a chance to get something I want, I move on it right away.',
	name: 'BISBAS12', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I feel pretty worried or upset when I think or know someone is angry at me.',
	name: 'BISBAS13', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I see an opportunity for something I like, I get excited right away.',
	name: 'BISBAS14', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I often act on the spur of the moment.',
	name: 'BISBAS15', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">If I think something unpleasant is going to happen, I usually get pretty worked up.',
	name: 'BISBAS16', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I often wonder why people act the way they do.',
	name: 'BISBAS17', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When good things happen to me, it affects me strongly.',
	name: 'BISBAS18', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I feel worried when I think I have done poorly at something.',
	name: 'BISBAS19', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I crave excitement and new sensations.',
	name: 'BISBAS20', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I go after something, I use a no holds barred approach.',
	name: 'BISBAS21', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I have very few fears compared to my friends.',
	name: 'BISBAS22', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">It would excite me to win a contest.',
	name: 'BISBAS23', 
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I worry about making mistakes.',
	name: 'BISBAS24', 
	labels: scale}
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var BIS_BAS = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order:false
};

var BISBAS_block = {
	timeline: [prompt, BIS_BAS],
	randomize_order: false,
};

