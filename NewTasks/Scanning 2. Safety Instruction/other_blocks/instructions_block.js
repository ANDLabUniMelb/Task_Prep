var instructions_block = {
	type:'instructions',
    pages: ['<p style="font-size:40px;">In this game, you will be shown pairs of animals and weapons.<p>' ,
    	'<p style="font-size:40px;">For each pair, <b>imagine the animal is trying to attack you.</b></p>' +
    	'<p style="font-size:40px;">Also <b>imagine you are defending yourself with the weapon.</b></p>' ,

    	'<p style="font-size:40px;">For some battles, you will see the animal that is attacking you first,</p> ' +
    	'<p style="font-size:40px;">for other battles you will see the weapon you are using to defend</p>' +
        '<p style="font-size:40px;">yourself first.</p>' ,

    	'<p style="font-size:40px;"><b>Your goal for each battle is to think about</b><p>'+
        '<p style="font-size:40px;"><b>whether you will win or lose.</b><p>',
    	'<br><p style="font-size:40px;">"Winning" does not necessarily mean killing the animal.</p>' +
        '<p style="font-size:40px;"><b>You can interpret "winning" as defeating the animal</b></p>' +
        '<p style="font-size:40px;"><b>either because it retreats or because you physically defeat it.</b></p>',
            
        '<p style="font-size:40px;"> For example: in this trial, you first see the animal - a gorilla</p>' +
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_gorilla + ' style="zoom: 90%;"/></td></tr>' +
		'</div>' +
		'<p style="font-size:40px;"> You will make an estimate of whether you win or lose</p>' +
        '<p style="font-size:40px;">the battle with the gorilla.</p>',
		'<p style="font-size:40px;"> <b>If you think you will win, you will press the RIGHT key,</b> </p>'+
		'<p style="font-size:40px;"><b> and if you think you will lose, you will press the LEFT key.</b> </p>'+
		'<p style="font-size:40px;">(Please press the LEFT key to go through the instructions for now.)</p>'+
            '<td><img src=' + instruction_buttons2 + ' style="zoom: 75%;"/></td></tr>' +
        '</div>',
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_gorilla + ' style="zoom: 90%;"/></td></tr>' +
		'</div>' +
		'<p style="font-size:40px;"> In this example, the gorilla is very strong, </p>'+
		'<p style="font-size:40px;">so most people would choose "lose" by pressing the LEFT key.</p>' ,

		'<p style="font-size:40px;"> If you see an animal as the first image,</p>'+
		'<p style="font-size:40px;"> next you will see the weapon you have.</p>',
		'<br><p style="font-size:40px;"> In this example, you received a rock as your weapon.</p>' +
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_rock + ' style="zoom: 90%;"/></td></tr>' +
		'</div>' ,
		'<p style="font-size:40px;"> Now that you know what weapon you have, </p>'+
		'<p style="font-size:40px;"><b>you can update your choice about whether you win or lose</b></p>'+
        '<p style="font-size:40px;"> <b>by pressing LEFT or RIGHT again. </b></p>',
		'<p style="font-size:40px;"> Most people would say they can\'t beat a gorilla with a rock, </p>'+
		'<p style="font-size:40px;">so they would choose "lose".</p>',

		'<p style="font-size:40px;"> After you make your second choice, you will see your outcome.</p>'+
		'<p style="font-size:40px;"><br> In this example, <b>you lost your battle</b> </p>'+
		'<p style="font-size:40px;"> because the gorilla is stronger than you fighting with a rock.</p>' ,
		'<p style="font-size:40px;">If you lose your battle, <b>you will hear an unpleasant sound.</b></p>'+
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_lost + ' style="zoom: 90%;"/></td></tr>' +
		'</div>',
		'<p style="font-size:40px;"> If you win your battle, <b>you will be safe and hear no sound.</b></p>'+
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_won + ' style="zoom: 90%;"/></td></tr>' +
		'</div>',

		'<p style="font-size:40px;">On some trials, you will see your weapon first.</p>',
		'<p style="font-size:40px;">In this example, you have a bow and arrow to battle with.</p>' +
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_bow + ' style="zoom: 90%;"/></td></tr>' +
		'</div>'+
        '<p style="font-size:40px;"><b>Press the RIGHT key if you think you will win</b></p>'+
        '<p style="font-size:40px;"><b>and the LEFT key if you think you will lose.</b></p>',
		'<p style="font-size:40px;"> You are battling a crow.<p>' +
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_crow + ' style="zoom: 90%;"/></td></tr>' +
		'</div>'+
        '<p style="font-size:40px;"><b> You can now update your choice about whether you win or lose. </b><p>',
        '<p style="font-size:40px;"><b> You won your battle</b> against the crow </p>'+
        '<p style="font-size:40px;"> with your bow and arrow.</p>' +
		    '</tr><tr style="height: 500px;">' +
            '<td><img src=' + instruction_won + ' style="zoom: 90%;"/></td></tr>' +
		'</div>'+
        '<p style="font-size:40px;"><b> You are safe and won\'t hear the unpleasant sound.</b></p>',

        '<p style="font-size:40px;"> For every animal and every weapon you will make a choice about </p>'+
        '<p style="font-size:40px;"> whether you think you will win or lose.</p>',
        '<p style="font-size:40px;"> <b> You won\'t always win your battle </b> when you\'re having'+
        '<p style="font-size:40px;"> a strong weapon or you\'re fighting with a weak animal.'+
        '<p style="font-size:40px;"><br> But <b>the likelihood of winning is better</b> the stronger'+
        '<p style="font-size:40px;"> your weapon is and the weaker your competitor is.',

		'<p style="font-size:40px;"> You will only have <b> 5 seconds</b> to make your </p>'+
        '<p style="font-size:40px;"> win/lose choices after seeing each image.</p>',
            
            
        '<p style="font-size:40px">Now you\'re ready to play a few practice rounds!</p>',],
    key_forward: 'c',
    key_backward: 'a'
};
