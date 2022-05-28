const express = require('express');
const path = require('path');
const fs = require('fs');

const APP_PORT = 8888;

const app = express();
app.use(express.json())

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.post("/pic", function(req, res){
	var dataUrl = req.body.dataUrl;
	buffer = Buffer.from(dataUrl.split(",")[1], 'base64');
	fs.writeFileSync("pic.jpg", buffer);
	console.log('odebrano zdjecie');
})

app.listen(APP_PORT, () => {
    console.log(`PORT: ${APP_PORT}`);
});
