const express = require('express')
const http = require('http')
const path = require('path');
const WebSocket = require('ws');

const PORT = 8888;
const app = express();

const serv = http.createServer(app);
const ws_server = new WebSocket.Server({ server: serv });

banned_ip = [];

ws_server.on("connection", ws => {
    ws.id = ws_server.getUniqueID();
    console.log(`POŁĄCZONO - ID: ${ws.id} ; IP: ${ws._socket.remoteAddress}`);

	ws_server.clients.forEach(function each(client) {
		if (client !== ws && client.readyState === WebSocket.OPEN) {
			client.send(`POŁĄCZONO NOWEGO USERA O ID ${ws.id}`);
		}
	});

    ws.onmessage = ({data}) => {
        console.log(`WIADOMOŚĆ - ID: ${ws.id} => ${data}`);
		
		//BANOWANIE
		if (data.substring(0,6) == "ZBANUJ"){
			let user = data.split("ZBANUJ ")[1];
			console.log(`BANUJEMY ${user}`);
			
			ws_server.clients.forEach(function each(client){
				if (client.id == user){
					banned_ip.push(client._socket.remoteAddress);
				}
			});
			
			console.log(`ZBANOWANE ADRESY: ${banned_ip}`);
		}
		
		ws_server.clients.forEach(function each(client) {
			if (banned_ip.includes(client._socket.remoteAddress)){
				console.log(`ZBANOWANY user ${ws.id}`);
				client.send(`ZBANOWANY`);
				client.close() //hmmmm...
			}
			else{
				if (client !== ws && client.readyState === WebSocket.OPEN) {
					client.send(`${ws.id}: ${data}`);
				}
			}
        });
    };

    ws.onclose = function(){
        console.log(`ROZŁĄCZON - ID: ${ws.id}`);

		ws_server.clients.forEach(function each(client) {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(`ROZŁĄCZONO USERA O ID ${ws.id}`);
            }
        });
    };
});

ws_server.getUniqueID = function (){
	var result = '';
	var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

	for ( var i=0; i<10; i++ ) {
		result += characters.charAt(Math.floor(Math.random() * characters.length));
	}
	return result;
};


app.get('/', (req, res) => {
	res.sendFile(path.join(__dirname, '/index.html'));
});

serv.listen(PORT, () => console.log(`Serwer na porcie ${PORT}`));
