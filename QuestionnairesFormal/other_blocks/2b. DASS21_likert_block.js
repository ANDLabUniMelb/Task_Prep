var prompt = {
    type: 'html-button-response',
	  stimulus: '<p style="font-size:24px">Please read each statement and decide how much it applies to you <b>in general</b>.</p>' +
        '<p style="font-size:24px"> There are no right or wrong answers.</p>'+
        '<p style="font-size:24px"> Do not spend too much time on any statement.</p>',
        choices: ['Continue']
};

var scale = [
    "Does not apply to me at all",
    "Applies to me to some degree, or some of the time",
    "Applies to me to a considerable degree, or a good part of the time",
    "Applies to me very much, or most of the time"
  ];
  
  var questions = [
    {prompt: '<p style="text-align:center; font-size:24px"><b>In general...</b></p><br>'+
    '<p style="text-align:center; font-size:24px">I find it hard to wind down.</p>',
    name: 'DASS1',
    labels: scale},
  
    {prompt: '<p style="text-align:center; font-size:24px">I am aware of dryness of my mouth.</p>',
    name: 'DASS2',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I can\'t seem to experience any positive feeling at all.</p>',
    name: 'DASS3',
    labels: scale},
    
    {prompt: '<p style="text-align:center; font-size:24px">I experience breathing difficulty (e.g., excessively rapid breathing, breathlessness in the absence of physical exertion).</p>',
    name: 'DASS4',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I find it difficult to work up the initiative to do things.</p>',
    name: 'DASS5',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I tend to over-react to situations.</p>',
    name: 'DASS6',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I experience trembling (e.g., in the hands).</p>',
    name: 'DASS7',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel that I use a lot of nervous energy.</p>',
    name: 'DASS8',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am worried about situations in which I might panic and make a fool of myself.</p>',
    name: 'DASS9',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel that I have nothing to look forward to.</p>',
    name: 'DASS10',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I find myself getting agitated.</p>',
    name: 'DASS11',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I find it difficult to relax.</p>',
    name: 'DASS12',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel down-hearted and blue.</p>',
    name: 'DASS13',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am intolerant of anything that keeps me from getting on with what I am doing.</p>',
    name: 'DASS14',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel I am close to panic.</p>',
    name: 'DASS15',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am unable to become enthusiastic about anything.</p>',
    name: 'DASS16',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel I am not worth much as a person.</p>',
    name: 'DASS17',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel that I am rather touchy.</p>',
    name: 'DASS18',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I am aware of the action of my heart in the absence of physical exertion (e.g., sense of heart rate increase, heart missing a beat).</p>',
    name: 'DASS19',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel scared without any good reason.</p>',
    name: 'DASS20',
    labels: scale},

    {prompt: '<p style="text-align:center; font-size:24px">I feel that life is meaningless.</p>',
    name: 'DASS21',
    labels: scale}
];

questions.forEach(function(question) {
    question.required = true;
});

var DASS21 = {
    type: 'survey-likert',
  	questions: questions,
    randomize_question_order: false
};
  
  var DASS21_block = {
    timeline: [prompt, DASS21],
    randomize_order: false,
  };
  