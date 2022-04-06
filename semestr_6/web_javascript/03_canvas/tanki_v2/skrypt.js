const cnvs = document.getElementById('canvas1');
cnvs.height = 600;
cnvs.width = 1000;
const ctx = cnvs.getContext('2d');
let restart = 0;
let tanks_arr = [];

//lepsze chyba tło jako img
let sky_colors = [];
//var rgba = new Uint8Array(cnvs.height*cnvs.width);
let rgba = [];

function start(){
	let players = document.getElementById("players").value;

    if(players < 2 || players > 5){
        alert("2 < players < 10");
        return;
    }

	if(restart==1){
		console.log("restart");
		window.location.reload();
	}
	
	draw_sky("blue", "red", 400);
	//save_color();
	draw_stars(1, 3, "#FFFFF0");
	draw_sun(15, 25, "#FF5733");
	array_xy = draw_mountains();
	draw_tank(players, array_xy);
	//console.log("function scope!!! " + array);
	//load_color2();
	console.log(tanks_arr);
	
	document.addEventListener('keypress', keyboard);

	restart++;
}

function draw_tank(how_many, arr){
	//console.log(arr);
	let tank_colors = ["yellow", "green", "blue", "pink", "white", "gray", "black"];
	for(let i=0; i<how_many; i++){
		rnd = randomize(5, arr.length-5);

		ctx.fillStyle = tank_colors[i];
		ctx.fillRect(arr[rnd][0], arr[rnd][1], 20, 10);
		ctx.fillRect(arr[rnd][0]+10, arr[rnd][1]-10, 2, 20); //barrel
		
		tanks_arr.push([arr[rnd][0], arr[rnd][1]]);
	}
}

function save_color(){
	//test
	imageData = ctx.getImageData(0, 0, cnvs.width, cnvs.height);

	for (let i=0; i+3<imageData.data.length; i+=4){
		//console.log(imageData.data[i]);
		rgba.push([imageData.data[i], imageData.data[i+1], imageData.data[i+2], imageData.data[i+3]]);
	}

	//console.log(imageData.data.length);
	console.log(rgba);
}

/*
function load_color(){
	//test
	console.log(rgba.lenght);
	ctx.clearRect(0, 0, cnvs.width, cnvs.height);
	for(let i=0; i<cvns.width; i++){
		for(let j=0; j<cnvs.height; j++){
			ctx.putImageData(rgba[i], i, j);
		}
	}
}

function load_color2(){
	data = new ImageData(rgba, cnvs.height, cnvs.width);
	ctx.putImageData(data, 0, 0, 0, 0, 0, 0);
}
*/

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
	var array = [];  //bez var/let tablica staje sie globalna

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

		if (i % 2 == 0 && i % 7 == 0){  //45 -> 600x400
			array.push([i, height]);
		}

		if (step > max_step){
			step = Math.random();
		}
		else if (height > 300){  //za wysoko
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
	//console.log(array);
	return array;
}

function randomize(min, max){
	//random int for other functions
	return Math.floor(Math.random() * (max - min) ) + min;
}

function keyboard(e){
	let button = e.code;

	if (button === 'KeyA')
		console.log("<-");

	if (button === 'KeyD')
		console.log("->");
}
