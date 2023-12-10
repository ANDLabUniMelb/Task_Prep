var prompt = {
    type: 'html-button-response',
    stimulus: '<p style="text-align:center; font-size:24px"><b>SCARED</b>' +
    '<p style="text-align:center; font-size:24px">For each sentence, please choose the response that seems to describe you most <b> for the last 3 months</b>.</p>',
    choices: ['Continue']
};

var scale = [
    "Not true or hardly ever true",
    "Somewhat true or sometimes true",
    "Very true or often true"
];

var questions = [
    {prompt: '<p style="text-align:center; font-size:24px"><b>For the last 3 months...</b></p><br>'+
        '<p style="text-align:center; font-size:24px">When I feel frightened, it is hard to breathe.</p>', name: 'SCARED1', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I get headaches when I am at school.</p>', name: 'SCARED2', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I do not like to be with people I do not know well.</p>', name: 'SCARED3', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I get scared if I sleep away from home.</p>', name: 'SCARED4', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about other people liking me.</p>', name: 'SCARED5', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, I feel like passing out.</p>', name: 'SCARED6', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am nervous.</p>', name: 'SCARED7', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I follow my mother or father wherever they go.</p>', name: 'SCARED8', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">People tell me that I look nervous.</p>', name: 'SCARED9', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel nervous with people I do not know well.</p>', name: 'SCARED10', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I get stomachaches at school.</p>', name: 'SCARED11', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, I feel like I am going crazy.</p>', name: 'SCARED12', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about sleeping alone.</p>', name: 'SCARED13', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about being as good as other kids.</p>', name: 'SCARED14', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, I feel like things are not real.</p>', name: 'SCARED15', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I have nightmares about something bad happening to my parents.</p>', name: 'SCARED16', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about going to school.</p>', name: 'SCARED17', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, my heart beats fast.</p>', name: 'SCARED18', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I get shaky.</p>', name: 'SCARED19', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I have nightmares about something bad happening to me.</p>', name: 'SCARED20', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about things working out for me.</p>', name: 'SCARED21', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, I sweat a lot.</p>', name: 'SCARED22', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am a worrier.</p>', name: 'SCARED23', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I get really frightened for no reason at all.</p>', name: 'SCARED24', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am afraid to be alone in the house.</p>', name: 'SCARED25', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">It is hard for me to talk with people I do not know well.</p>', name: 'SCARED26', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, I feel like I am choking.</p>', name: 'SCARED27', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">People tell me that I worry too much.</p>', name: 'SCARED28', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I do not like to be away from my family.</p>', name: 'SCARED29', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am afraid of having anxiety (or panic) attacks.</p>', name: 'SCARED30', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry that something bad might happen to my parents.</p>', name: 'SCARED31', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel shy with people I do not know well.</p>', name: 'SCARED32', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about what is going to happen in the future.</p>', name: 'SCARED33', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, I feel like throwing up.</p>', name: 'SCARED34', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about how well I do things.</p>', name: 'SCARED35', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am scared to go to school.</p>', name: 'SCARED36', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I worry about things that have already happened.</p>', name: 'SCARED37', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">When I get frightened, I feel dizzy.</p>', name: 'SCARED38', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel nervous when I am with other children or adults and I have to do something while they watch me (for example: read aloud, speak, play a game, play a sport).</p>', name: 'SCARED39', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I feel nervous when I am going to parties, dances, or any place where there will be people that I don’t know well.</p>', name: 'SCARED40', labels: scale},
    {prompt: '<p style="text-align:center; font-size:24px">I am shy.</p>', name: 'SCARED41', labels: scale},
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var SCARED = {
    type: 'survey-likert',
    questions: questions,
    randomize_question_order: false
};

var SCARED_block = {
    timeline: [prompt, SCARED],
    randomize_order: false,
};
