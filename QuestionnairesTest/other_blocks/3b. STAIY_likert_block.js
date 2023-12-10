var prompt = {
    type: 'html-button-response',
    stimulus: '<p style="text-align:center; font-size:24px"><b>STAIY</b>' +
    '<p style="text-align:center; font-size:24px">A number of statements which people have used to describe themselves are given below.</p>' +
        '<p style="text-align:center; font-size:24px">Read each statement and then choose the appropriate response to indicate how you feel right now, that is, <b>at this moment</b>.</p>' +
        '<p style="text-align:center; font-size:24px">There are no right or wrong answers.</p>',
		choices: ['Continue']
};

var scale = [
    "Not at all",
    "Somewhat",
    "Moderately so",
    "Very much so"
];

var questions = [
    {prompt: '<p style="text-align:center; font-size:24px"><b>At this moment...</b></p><br>'+
    '<p style="text-align:center; font-size:24px">I feel calm.', name: 'STAIY1', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel secure.', name: 'STAIY2', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am tense.', name: 'STAIY3', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel strained.', name: 'STAIY4', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel at ease.', name: 'STAIY5', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel upset.', name: 'STAIY6', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am presently worrying over possible misfortunes.', name: 'STAIY7', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel satisfied.', name: 'STAIY8', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel frightened.', name: 'STAIY9', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel comfortable.', name: 'STAIY10', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel self-confident.', name: 'STAIY11', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel nervous.', name: 'STAIY12', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am jittery.', name: 'STAIY13', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel indecisive.', name: 'STAIY14', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am relaxed.', name: 'STAIY15', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel content.', name: 'STAIY16', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am worried.', name: 'STAIY17', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel confused.', name: 'STAIY18', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel steady.', name: 'STAIY19', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel pleasant.', name: 'STAIY20', labels: scale}
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var STAIY = {
    type: 'survey-likert',
    questions: questions,
    randomize_question_order: false
};

var STAIY_block = {
    timeline: [prompt, STAIY],
    randomize_order: false,
};
