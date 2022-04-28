const http = require('http');
var fs = require('fs');
const { parse } = require('querystring');

const PORT = 8088;

/*
const server = http.createServer((req, res) => {
    if (req.method === 'POST') {
        collectRequestData(req, result => {
            console.log(result);
            res.end(`${result.username} napisał komentarz: ${result.komentarz}`);
        });
    } 
    else {
        res.end(`
            <!doctype html>
            <html>
            <body>
                <form action="/" method="post">
                    <input type="text" name="username" /><br />
                    <input type="text" name="komentarz" /><br />
                    <button>OK</button>
                </form>
            </body>
            </html>
        `);
    }
});
server.listen(PORT);
*/

fs.readFile('./index.html', function(err, html){
	if (err) throw err;

	http.createServer(function (req, res){
		res.writeHead(200, {'Content-Type': 'text/html'});
		res.write(html);

		if (req.method === 'POST') {
			collectRequestData(req, result => {
				var d = new Date();
				var time = d.toLocaleTimeString();
				var date = d.toLocaleDateString();
				
				var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress || req.socket.remoteAddress ||
				(req.connection.socket ? req.connection.socket.remoteAddress : null);
				
				let user = result.username;
				let koment = result.komentarz;

				//zapisywanie wszystkiego do pliku
				var dopliku = "Użytkownik: <b>"+user+"</b><br>IP: <b>"+ip.substring(7)+"</b><br>Dodano: <i>"
							  +date+" "+time+"</i><br> Komentarz: <i>"+koment+"</i><br><br>\n";
				console.log(dopliku);
				fs.appendFile('onetannodomini2005.html', dopliku, function (err){
					if (err) throw err;
					console.log('Zapisano!');
				});
			});
		}
		
		fs.readFile('./onetannodomini2005.html', function(err, html_koment){
			if (err) throw err;
			return res.end(html_koment + 
			`<br>
			<div id="dodaj_komentarz">
				<h1>Dodaj komentarz:</h1>
				<form action="http://127.0.0.1:8088" method="POST">
					<label for="user">Nick:</label><br>
					<input type="text" id="username" name="username"><br>
					
					<label for="komentarz">Komentarz:</label><br>
					<textarea id="komentarz" name="komentarz" rows="10" cols="30"></textarea><br>

					<button type="submit">OK</button>
					
				</form>
			</div>`
			);
		});

	}).listen(PORT);
});

function collectRequestData(request, callback) {
    const FORM_URLENCODED = 'application/x-www-form-urlencoded';
    if(request.headers['content-type'] === FORM_URLENCODED) {
        let body = '';
        request.on('data', chunk => {
            body += chunk.toString();
        });
        request.on('end', () => {
            callback(parse(body));
        });
    }
    else {
        callback(null);
    }
}