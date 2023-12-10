var prompt = {
	type: 'html-button-response',
	stimulus: '<p style="text-align:center; font-size:24px"><b>AFML</b>' +
	'<p style="text-align:center; font-size:24px">Rate each item on a 5-point Likert-scale ranging from 1 (Strongly Disagree) to 5 (Strongly Agree).</p>',
	choices: ['Continue']
};

var scale = [
	"Strongly Disagree",
	"Disagree",
	"Neutral",
	"Agree",
	"Strongly Agree"
];

var questions = [
	{prompt: '<p style="text-align:center; font-size:24px">Listening to music distracts me from stress.',
	name: 'AFML1',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel stressed listening to music helps to take my mind off it.',
	name: 'AFML2',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I can escape from stressful situations by listening to music.',
	name: 'AFML3',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel stressed I get comfort from listening to music.',
	name: 'AFML4',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I feel intense emotions.',
	name: 'AFML5',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I feel a range of emotions.',
	name: 'AFML6',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I feel emotions deeply.',
	name: 'AFML7',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I feel a variety of emotions simultaneously.',
	name: 'AFML8',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I feel a mixture of many different emotions.',
	name: 'AFML9',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I feel strong emotions when listening to music.',
	name: 'AFML10',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel sad/depressed listening to music makes me dwell upon those feelings.',
	name: 'AFML11',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel sad/depressed listening to music leads me to focus on those feelings.',
	name: 'AFML12',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious listening to music makes me dwell upon those feelings.',
	name: 'AFML13',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious listening to music leads me to focus on those feelings.',
	name: 'AFML14',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music in bed helps me fall asleep.',
	name: 'AFML15',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I listen to music in bed because it helps me get to sleep.',
	name: 'AFML16',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music does not bring back memories for me.',
	name: 'AFML17',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I reminisce about the past.',
	name: 'AFML18',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I remember my past.',
	name: 'AFML19',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music reminds me of people from my past.',
	name: 'AFML20',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel angry listening to music helps me look on the bright side.',
	name: 'AFML21',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel angry listening to music helps me see things in a more positive light.',
	name: 'AFML22',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel angry listening to music helps to take my mind off it.',
	name: 'AFML23',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel angry music distracts me from feelings of anger.',
	name: 'AFML24',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel angry I listen to music that makes me happy.',
	name: 'AFML25',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel angry listening to my favorite music makes me feel happier.',
	name: 'AFML26',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel angry I get comfort from listening to music.',
	name: 'AFML27',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious listening to music helps me look on the bright side.',
	name: 'AFML28',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious listening to music helps me see things in a more positive light.',
	name: 'AFML29',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious listening to my favorite music makes me feel happier.',
	name: 'AFML30',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious I listen to music that makes me happy.',
	name: 'AFML31',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music distracts me from feelings of anxiety.',
	name: 'AFML32',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious listening to music helps to take my mind off it.',
	name: 'AFML33',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When I feel anxious I get comfort from listening to music.',
	name: 'AFML34',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music I feel a sense of awe for the talent of the composer.',
	name: 'AFML35',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music I feel a sense of awe for the talent of the performer.',
	name: 'AFML36',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">When listening to music I do not admire the talent of the performers.',
	name: 'AFML37',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">I feel less lonely when I listen to music.',
	name: 'AFML38',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music reduces feelings of loneliness.',
	name: 'AFML39',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music makes me feel less alone.',
	name: 'AFML40',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Playing music in the background helps me to concentrate.',
	name: 'AFML41',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Having background music makes it easier to focus on what I\'m doing.',
	name: 'AFML42',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Music listening is a fundamental part of who I am.',
	name: 'AFML43',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">The music I listen to expresses who I am as a person.',
	name: 'AFML44',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music has helped me discover who I am.',
	name: 'AFML45',
	labels: scale},

	{prompt: '<p style="text-align:center; font-size:24px">Listening to music has helped me to understand myself.',
	name: 'AFML46',
	labels: scale}
];

// questions.forEach(function(question) {
//     question.required = true;
// });

var AFML = {
	type: 'survey-likert',
	questions: questions,
	randomize_question_order: false
};

var AFML_block = {
	timeline: [prompt, AFML],
	randomize_order: false
};
