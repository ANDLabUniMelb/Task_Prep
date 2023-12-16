var prompt = {
    type: 'html-button-response',
    stimulus: '<p style="text-align:center; font-size:24px">Please respond to the following statements using these response categories: "Not at all true", "Hardly true", "Moderately true", or "Exactly true".</p>',
    choices: ['Continue']
};

var scale = [
    "Not at all true",
    "Hardly true",
    "Moderately true",
    "Exactly true"];
 
var questions = [
    {prompt: '<p style="text-align:center; font-size:24px">I can always manage to solve difficult problems if I try hard enough.',
    name: 'GSE1',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">If someone opposes me, I can find the means and ways to get what I want.',
    name: 'GSE2',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">It is easy for me to stick to my aims and accomplish my goals.',
    name: 'GSE3',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am confident that I could deal efficiently with unexpected events.',
    name: 'GSE4',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">Thanks to my resourcefulness, I know how to handle unforeseen situations.',
    name: 'GSE5',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I can solve most problems if I invest the necessary effort.',
    name: 'GSE6',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I can remain calm when facing difficulties because I can rely on my coping abilities.',
    name: 'GSE7',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I am confronted with a problem, I can usually find several solutions.',
    name: 'GSE8',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">If I am in trouble, I can usually think of a solution.',
    name: 'GSE9',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I can usually handle whatever comes my way.',
    name: 'GSE10',
    labels: scale}
];

questions.forEach(function(question) {
  question.required = true;
});

var GSE = {
    type: 'survey-likert',
    questions: questions,
    randomize_question_order:false
};
 
var GSE_block = {
	  timeline: [prompt, GSE],
	  randomize_order: false,
};
