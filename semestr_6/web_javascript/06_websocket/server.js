const WebSocket = require("ws");
const ws_server = new WebSocket.Server({port: 8089});

ws_server.on("connection", ws => {
    ws.id = ws_server.getUniqueID();
    console.log(`POŁĄCZONO - ID: ${ws.id}`);
	
	ws_server.clients.forEach(function each(client) {
		if (client !== ws && client.readyState === WebSocket.OPEN) {
			client.send(`POŁĄCZONO id usera: ${ws.id}`);
		}
	});

    ws.onmessage = ({data}) => {
        console.log(`WIADOMOŚĆ - ID: ${ws.id} => ${data}`);
        
		ws_server.clients.forEach(function each(client) {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(`${data}`);
            }
        });
    };

    ws.onclose = function(){
        console.log(`ROZŁĄCZON - ID: ${ws.id}`);

		ws_server.clients.forEach(function each(client) {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(`ROZŁĄCZONO id usera: ${ws.id}`);
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