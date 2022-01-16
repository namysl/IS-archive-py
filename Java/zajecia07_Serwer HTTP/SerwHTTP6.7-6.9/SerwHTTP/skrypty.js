let saveFile = () => {
const name = document.getElementById('name');
const info = document.getElementById('info');
let data =
'\r Imie: \n' + name.value + ' \r\n\n ' +
'Wiadomosc:\n' + info.value;
const textToBLOB = new Blob([data], { type: 'text/plain' });
const sFileName = 'nowa_wiadomosc.txt';
let newLink = document.createElement("a");
newLink.download = sFileName;
if (window.webkitURL != null) {
newLink.href = window.webkitURL.createObjectURL(textToBLOB);
}
else {
newLink.href = window.URL.createObjectURL(textToBLOB);
newLink.style.display = "none";
document.body.appendChild(newLink);
}
newLink.click();
}
	

function logIn(form) {
if (form.name.value=='user') { 
if (form.password.value=='1234') {              
location='udane_logowanie.html'
} else {
alert('Niepoprawne hasło')
}
} else {alert('Niepoprawna nazwa użytkownika');
}
}
