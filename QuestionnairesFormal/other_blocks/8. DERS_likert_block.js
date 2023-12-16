var prompt = {
    type: 'html-button-response',
    stimulus: '<p style="text-align:center; font-size:24px"> Please indicate how often the following apply to you. </p>',
    choices: ['Continue']
};

var scale = [
    "Almost never (0-10%)",
    "Sometimes (11-35%)",
    "About half of the time (36-65%)",
    "Most of the time (66-90%)",
    "Almost always (91-100%)"
];

var questions = [
    {prompt: '<p style="text-align:center; font-size:24px"> I pay attention to how I feel.</p>',
    name: 'DERS1',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> I have no idea how I am feeling.</p>',
    name: 'DERS2',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> I have difficulty making sense out of my feelings.</p>',
    name: 'DERS3',
    labels: scale},
    
    {prompt: '<p style="text-align:center; font-size:24px"> I care about what I am feeling.</p>',
    name: 'DERS4',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> I am confused about how I feel.</p>',
    name: 'DERS5',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I acknowledge my emotions.</p>',
    name: 'DERS6',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I become embarrassed for feeling that way.</p>',
    name: 'DERS7',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I have difficulty getting work done.</p>',
    name: 'DERS8',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I become out of control.</p>',
    name: 'DERS9',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I believe that I will end up feeling very depressed.</p>',
    name: 'DERS10',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I have difficulty focusing on other things.</p>',
    name: 'DERS11',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I feel guilty for feeling that way.</p>',
    name: 'DERS12',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I have difficulty concentrating.</p>',
    name: 'DERS13',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I have difficulty controlling my behaviors.</p>',
    name: 'DERS14',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I believe there is nothing I can do to make myself feel better.</p>',
    name: 'DERS15',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I become irritated at myself for feeling that way.</p>',
    name: 'DERS16',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, I lose control over my behavior.</p>',
    name: 'DERS17',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px"> When I am upset, it takes me a long time to feel better.</p>',
    name: 'DERS18',
    labels: scale},
];

questions.forEach(function(question) {
    question.required = true;
});

var DERS = {
    type: 'survey-likert',
    questions: questions,
    randomize_question_order: false
};

var DERS_block = {
    timeline: [prompt, DERS],
    randomize_order: false,
};
