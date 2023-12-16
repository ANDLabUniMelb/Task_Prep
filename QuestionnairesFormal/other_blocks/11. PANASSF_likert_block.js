var prompt = {
    type: 'html-button-response',
    stimulus:	'<p style="text-align:center; font-size:24px">Indicate the extent you have felt this way <b>over the past week</b>.</p>',
		choices: ['Continue']
};

var scale = [
    "Very slightly or not at all",
    "A little",
    "Moderately",
    "Quite a bit",
    "Extremely"
];

var questions = [
    {prompt: '<p style="text-align:center; font-size:24px"><b>Over the past week, I felt...</b></p><br>'+
    '<p style="text-align:center; font-size:24px">Interested', name: 'PANAS1', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Distressed', name: 'PANAS2', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Excited', name: 'PANAS3', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Upset', name: 'PANAS4', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Strong', name: 'PANAS5', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Guilty', name: 'PANAS6', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Scared', name: 'PANAS7', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Hostile', name: 'PANAS8', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Enthusiastic', name: 'PANAS9', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Proud', name: 'PANAS10', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Irritable', name: 'PANAS11', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Alert', name: 'PANAS12', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Ashamed', name: 'PANAS13', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Inspired', name: 'PANAS14', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Nervous', name: 'PANAS15', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Determined', name: 'PANAS16', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Attentive', name: 'PANAS17', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Jittery', name: 'PANAS18', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Active', name: 'PANAS19', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">Afraid', name: 'PANAS20', labels: scale}
];

questions.forEach(function(question) {
  question.required = true;
});

var PANASSF = {
	type: 'survey-likert',
  questions: questions,
  randomize_question_order: false
};

var PANASSF_block = {
timeline: [prompt, PANASSF],
randomize_order: false
};
