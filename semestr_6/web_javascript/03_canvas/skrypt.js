//scorched earth

document.onkeydown = checkKey;
document.onmousemove = mouseev;
document.onmousedown = mouseevd;
document.onmouseup = mouseevu;

var x=100; y=100; en=0;

const cnvs = document.getElementById('canvas1');
const ctx = cnvs.getContext('2d');

draw_sky("blue", "red", 400);
draw_stars(1, 3, "#FFFFF0");
draw_sun(15, 25, "#FF5733");
draw_mountains();


function draw_sky(color1, color2, y_color_change){
	var gradient = ctx.createLinearGradient(0, 0, 0, y_color_change);
	gradient.addColorStop(0, color1);
	gradient.addColorStop(1, color2);

	ctx.fillStyle = gradient;
	ctx.fillRect(0, 0, cnvs.width, cnvs.height);
}

function draw_stars(range1, range2, color){
	let rnd = randomize(10, 40);
	
	for(let i=0; i<rnd; i++){
		draw_sun(range1, range2, color);
	}
}

function draw_sun(range1, range2, color){
	let rnd_x = randomize(0, cnvs.width);
	let rnd_y = randomize(0, cnvs.height/2);
	let rnd_size = randomize(range1, range2);
	
	var circle = new Path2D();

	circle.arc(rnd_x, rnd_y, rnd_size, 0, 2 * Math.PI);
	
	ctx.shadowBlur = 50;
	ctx.shadowColor = "white";
	ctx.fillStyle = color;
	ctx.fill(circle);
}

function draw_mountains(){
	ctx.shadowBlur = 0;
	var gradient = ctx.createLinearGradient(0, 0, 0, 500);
	gradient.addColorStop(0, "red");
	gradient.addColorStop(1, "black");
	ctx.fillStyle = gradient;
	
	ctx.translate(0.5, 50);  //przesun

	let height = randomize(0, cnvs.height);

	let step = Math.random();  //poczatkowe nachylenie [0, 1)
	let change_step = 0.5;  //zmiana nachylenia w kroku
	let max_step = 5;
	
	for (let i=0; i<cnvs.width; i++) {
		height += step;
		add_step =  change_step - 2*(change_step * Math.random());
		step += add_step;

		if (step > max_step){
			step = Math.random();
		}
		else if (height > 500){  //za wysoko
			step *= -1;
			height -= 5;
		}
		else if (height < 150) {  //za nisko
			step *= -1;
			step += 5;
		}

		//ctx.beginPath();
		ctx.moveTo(i, cnvs.height);
		ctx.lineTo(i, height);
		ctx.strokeStyle = gradient;
		ctx.stroke();
	}
}

function randomize(min, max){
    //random for other functions
	return Math.floor(Math.random() * (max - min) ) + min;
}

function checkKey(e){
	//when the user is pressing a key
	e=e||window.event;
	
	if (e.keyCode=='38'){y--;}
	else if (e.keyCode=='40'){y++;}
	else if (e.keyCode=='37'){x--;}
	else if (e.keyCode=='39'){x++;}
	if (x<0)    x = 0;
	if (y<0)    y = 0;
	if (x>1000) x = 1000; 
	if (y>600)  y = 600;

	ctx.clearRect(x, y, 5, 5);
}

function mouseev(e){
	//when the pointer is moving while it is over an element
	x=e.clientX;
	y=e.clientY;
	if (x<0)   x = 0;
	if (y<0)   y = 0;
	if (x>1000) x = 1000;
	if (y>600) y = 600;
	if (en==1) ctx.fillRect(x, y, 2, 2);
}

function mouseevd(e){
	//when the user presses a mouse button over an element
	en = 1;
	x = e.clientX;
	y = e.clientY;

    if ((x>360)&&(x<400)){
	    if (y<40) 			   ctx.fillStyle="#FF0000";
	    if ((y>40)&&(y<=80))   ctx.fillStyle="#00FF00";
	    if ((y>80)&&(y<=120))  ctx.fillStyle="#0000FF";
	    if ((y>120)&&(y<=160)) ctx.fillStyle="#000000";
	}
}

function mouseevu(e){
    //when a user releases a mouse button over an element
	en = 0;
}
