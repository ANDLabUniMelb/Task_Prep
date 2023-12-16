var prompt = {
    type: 'html-button-response',
    stimulus: '<p style="text-align:center; font-size:24px">Below is a list of sentences that describe how people feel.</p>'+
    '<p style="text-align:center; font-size:24px">Read each phase and decide if it is "Not true or hardly ever true" or "Somewhat true or sometimes true" or "Very true or often true" for you.</p>'+
    '<p style="text-align:center; font-size:24px">For each sentence, please choose the answer that corresponds to the response that seems to describe you <b>now or within the past 3 months</b>.</p>',

    choices: ['Continue']
};




var scale = [
    "Not true or hardly ever true",
    "Somewhat true or sometimes true",
    "Very true or often true"
];

var questions = [
    {prompt: '<p style="text-align:center; font-size:24px"><b>For now or within the past 3 months...</b></p><br>'+
        '<p style="text-align:center; font-size:24px">When I feel nervous, it is hard for me to breathe.</p>',
        name: 'SCAARED1',
        labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I get headaches when I am at school, at work, or in public places.</p>',
    name: 'SCAARED2',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I do not like to be with people I do not know well.</p>',
    name: 'SCAARED3',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I get nervous if I sleep away from home.</p>',
    name: 'SCAARED4',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about people liking me.</p>',
    name: 'SCAARED5',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, I feel like passing out.</p>',
    name: 'SCAARED6',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am nervous.</p>',
    name: 'SCAARED7',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">It is hard for me to stop worrying.</p>',
    name: 'SCAARED8',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">People tell me that I look nervous.</p>',
    name: 'SCAARED9',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel nervous with people I do not know well.</p>',
    name: 'SCAARED10',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I get stomachaches at school, at work, or in public places.</p>',
    name: 'SCAARED11',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, I feel like I am going crazy.</p>',
    name: 'SCAARED12',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about sleeping alone.</p>',
    name: 'SCAARED13',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about being as good as other people.</p>',
    name: 'SCAARED14',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, I feel like things are not real.</p>',
    name: 'SCAARED15',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I have nightmares about something bad happening to my family.</p>',
    name: 'SCAARED16',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about going to work or school or to public places.</p>',
    name: 'SCAARED17',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, my heart beats fast.</p>',
    name: 'SCAARED18',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I get shaky.</p>',
    name: 'SCAARED19',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I have nightmares about something bad happening to me.</p>',
    name: 'SCAARED20',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about things working out for me.</p>',
    name: 'SCAARED21',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, I sweat a lot.</p>',
    name: 'SCAARED22',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am a worrier.</p>',
    name: 'SCAARED23',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I worry a lot, I have trouble sleeping.</p>',
    name: 'SCAARED24',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I get really frightened for no reason at all.</p>',
    name: 'SCAARED25',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am afraid to be alone in the house.</p>',
    name: 'SCAARED26',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">It is hard for me to talk with people I do not know well.</p>',
    name: 'SCAARED27',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, I feel like I am choking.</p>',
    name: 'SCAARED28',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">People tell me that I worry too much.</p>',
    name: 'SCAARED29',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I do not like to be away from my family.</p>',
    name: 'SCAARED30',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I worry a lot, I feel restless.</p>',
    name: 'SCAARED31',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am afraid of having anxiety (or panic) attacks.</p>',
    name: 'SCAARED32',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry that something bad might happen to my family.</p>',
    name: 'SCAARED33',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel shy with people I do not know well.</p>',
    name: 'SCAARED34',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about what is going to happen in the future.</p>',
    name: 'SCAARED35',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, I feel like throwing up.</p>',
    name: 'SCAARED36',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about how well I do things.</p>',
    name: 'SCAARED37',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am afraid to go outside or to crowded places by myself.</p>',
    name: 'SCAARED38',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I worry about things that have already happened.</p>',
    name: 'SCAARED39',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">When I get anxious, I feel dizzy.</p>',
    name: 'SCAARED40',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel nervous when I am with other people and I have to do something while they watch me (for example: speak, play a sport).</p>',
    name: 'SCAARED41',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel nervous when I go to parties, dances, or any place where there will be people that I do not know well.</p>',
    name: 'SCAARED42',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am shy.</p>',
    name: 'SCAARED43',

    labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I worry a lot, I feel irritable.</p>',
    name: 'SCAARED44',
    labels: scale}
];

questions.forEach(function(question) {
    question.required = true;
});

var SCAARED = {
    type: 'survey-likert',
    questions: questions,
    randomize_question_order: false
};

var SCAARED_block = {
    timeline: [prompt, SCAARED],
    randomize_order: false,
};
