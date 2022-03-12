//scorched earth

document.onkeydown = checkKey;
document.onmousemove = mouseev;
document.onmousedown = mouseevd;
document.onmouseup = mouseevu;

var x=100; y=100; en=0;

const cnvs = document.getElementById('canvas1');
const ctx = cnvs.getContext('2d');

ctx.fillStyle = "#6D0000";
ctx.fillRect(0, 0, 700, 500);

ctx.fillStyle = "#555000";
ctx.fillRect(100, 100, 100, 100);
ctx.fillStyle = "#000000";

let rnd = 600;


for(let i=0; i<700; i++){
	let a = 2;
	if(i % 7 == 0 && i % 5 == 0){
        rnd = randomize(400, 500);
	}
	
	ctx.fillStyle = "#000000";
	draw_terrain(i, 700-rnd+a, 1, rnd+a);
	a += 100;
}

//    for(let i=0; i<10; i++){
//	draw(i*i, i*i, i*i, i*i);
//    }

function draw_terrain(x, y, width, height){
//	const canvas = document.getElementById('canvas1');
//	const ctx = canvas.getContext('2d');

	ctx.fillRect(x, y, width, height);
}

function randomize(min, max){
    	// eh
	return Math.floor(Math.random() * (max - min) ) + min;
}

function checkKey(e){
	//when the user is pressing a key
	e=e||window.event;
	if (e.keyCode=='38'){y--;}
	else if (e.keyCode=='40'){y++;}
	else if (e.keyCode=='37'){x--;}
	else if (e.keyCode=='39'){x++;}
	if (x<0) x=0;
	if (y<0) y=0;
	if (x>500) x=500; 
	if (y>500) x=500;

	ctx.clearRect(x,y,5,5);
}

function mouseev(e){
	//when the pointer is moving while it is over an element
	x=e.clientX;
	y=e.clientY;
	if (x<0) x=0;
	if (y<0) y=0;
	if (x>500) x=500;
	if (y>500) x=500;
	if (en==1) ctx.fillRect(x,y,2,2);
}

function mouseevd(e){
	//when the user presses a mouse button over an element
	en=1;
	x=e.clientX;
	y=e.clientY;

    if ((x>360) && (x<400)){
	    if (y<40) ctx.fillStyle="#FF0000";
	    if ((y>40)&&(y<=80)) ctx.fillStyle="#00FF00";
	    if ((y>80)&&(y<=120)) ctx.fillStyle="#0000FF";
	    if ((y>120)&&(y<=160)) ctx.fillStyle="#000000";
	}
}

function mouseevu(e){
    	//when a user releases a mouse button over an element
	en=0;
}
