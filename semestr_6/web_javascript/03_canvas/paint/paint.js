document.onkeydown=checkKey;
document.onmousemove=mouseev;
document.onmousedown=mouseevd;
document.onmouseup=mouseevu;
var x=100; y=100; en=0;

const aaa=document.getElementById('canvas1');
const ctx=aaa.getContext('2d');
ctx.fillStyle="#6D0000";
ctx.fillRect(0,0,400,400);

ctx.fillStyle="#FF0000";
ctx.fillRect(360,0,400,40);
ctx.fillStyle="#00FF00";
ctx.fillRect(360,40,400,80);
ctx.fillStyle="#0000FF";
ctx.fillRect(360,80,400,120);
ctx.fillStyle="#000000";
ctx.fillRect(360,120,400,160);
ctx.font="italic bold 30px  Arial";
ctx.fillText("tekst",10,40);

function checkKey(e){
	e=e||window.event;
	if (e.keyCode=='38'){y--;}
	else if (e.keyCode=='40'){y++;}
	else if (e.keyCode=='37'){x--;}
	else if (e.keyCode=='39'){x++;}
	if (x<0) x=0; if (y<0) y=0;
	if (x>400) x=400; if (y>400) x=400;

	ctx.clearRect(x,y,5,5);
}

function mouseev(e){
	x=e.clientX;
	y=e.clientY;
	if (x<0) x=0; if (y<0) y=0;
	if (x>400) x=400; if (y>400) x=400;
	if (en==1) ctx.fillRect(x,y,2,2);
}

function mouseevd(e){en=1;
	x=e.clientX;
	y=e.clientY;
    if ((x>360) && (x<400)) {
if (y<40) ctx.fillStyle="#FF0000";
if ((y>40)&&(y<=80)) ctx.fillStyle="#00FF00";
if ((y>80)&&(y<=120)) ctx.fillStyle="#0000FF";
if ((y>120)&&(y<=160)) ctx.fillStyle="#000000";




}

 }
function mouseevu(e){en=0;}

