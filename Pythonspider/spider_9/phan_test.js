var page = require('webpage').create(),
    system =require ('system'),
    t,address;

if(system.args.length ===1 ){
	console.log('Usage:phan_test.js <some URL>');
	phantom.exit();
}

//t =Date.now();
t = new Date();
address =system.args[1];

page.open(address,function(status){
		console.log('Status:' + status);
		if (status === 'success'){
			t = Date.now() - t;
			console.log('Loading ' + system.args[1]);
			console.log('Loading time '+ t +' msec');
			//page.render('12.jpg');
		}
		phantom.exit();
		});
