var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {
	 		        res.writeHead(200, {'Content-Type': 'text/html'});
			        res.write('Taka sobie strona');
var ip = req.headers['x-forwarded-for'] || 
     req.connection.remoteAddress || 
     req.socket.remoteAddress ||
     (req.connection.socket ? req.connection.socket.remoteAddress : null);
fs.appendFile('ip.txt', ip+"\n", function (err) {
	  if (err) throw err;
	  console.log('Zapisano!');
}); 


			        return res.end();
			      }
).listen(8080); 
