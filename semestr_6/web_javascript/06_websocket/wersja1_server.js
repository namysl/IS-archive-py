const express = require('express')

const WebSocket = require("ws");
const ws_server = new WebSocket.Server({port: 8089});

const app = express();
const PORT = 8090;  // http://127.0.0.1:8090

app.listen(PORT, () => console.log(`Serwer na porcie ${PORT}`));

const path = require('path');
app.use(express.static(path.join(__dirname, 'public')));



ws_server.on("connection", ws => {
    ws.id = ws_server.getUniqueID();
    console.log(`POŁĄCZONO - ID: ${ws.id}`);
	
	ws_server.clients.forEach(function each(client) {
		if (client !== ws && client.readyState === WebSocket.OPEN) {
			client.send(`POŁĄCZONO NOWEGO USERA O ID ${ws.id}`);
		}
	});

    ws.onmessage = ({data}) => {
        console.log(`WIADOMOŚĆ - ID: ${ws.id} => ${data}`);
        
		ws_server.clients.forEach(function each(client) {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(`${ws.id}: ${data}`);
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