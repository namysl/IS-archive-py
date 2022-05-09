const server_port = 8888;
console.log("Port: " + server_port);
	
const http = require('http');
const fs = require('fs');
const url = require('url');

const db_port = "mongodb://localhost:27017/";
const MongoDBClient = require('mongodb').MongoClient;
const ObjectId = require('mongodb').ObjectID;

let str = "";
let poprzedni = "";

http.createServer((req, res) => {
    const url_req = url.parse(req.url, true);
    const user_query = url_req.query;
	
	//req.url -> to co jest po 8888/
	//user_query -> to co jest po ? w url			

	let nowy;
	if(url_req.search){
		nowy = url_req.search.substring(1);
		console.log("SEARCH: " + url_req.search + " NOWY: " + nowy);
	}
	else{
		nowy = "";
	}
	
    if (nowy.startsWith('n') || poprzedni != "") {
		console.log("DODAJE NOWY REKORD!!! nowy: ", nowy);
        nowy = poprzedni;
    }
    poprzedni = nowy;

	//console.log("url: " + req.url + " nowy: " + nowy + " poprzedni: " + poprzedni);
	console.log(user_query);
	
    load_from_DB();
	
	if(url_req.path === "/index.html" || url_req.path === "/"){
		nowy = "";
		poprzedni = "";
		load_html_db("./index.html", str);
	}
	else if(url_req.path === "/index.html?" + nowy){
		delete_from_DB(nowy);
		nowy = "";
		poprzedni = "";
		load_html_db("./index.html", str);
	}
	else{
		if (url_req.path.substring(0, 4) == "/add"){ //czy na pewno dodawanie
			load_html_db("./addnewrecord.html", "");
			if(user_query.new1 && user_query.new2 && user_query.new3){
				add_to_DB(user_query);
			}
		}
	}

    function load_html_db(plik, str) {
        fs.readFile(plik, (err, db_records) => {
            if (err) throw err;

            res.writeHead(200, {'Content-Type': 'text/html'});
            let db_records_str = String(db_records);
            let htmlpage = db_records_str.replace("<!--tutajbaza-->", str);
            res.write(htmlpage);
            res.end();
        });
    };

    function load_from_DB() {
        MongoDBClient.connect(db_port, {useNewUrlParser: true, useUnifiedTopology: true}, (err, db) => {
            if (err) throw err;

            const mojaDB = db.db("mojabaza");
			
			let i = 1;
			str = "";
            mojaDB.collection("input").find({}).toArray((err, found) => {
                if (err) throw err; 

                found.forEach(item => {
                    str += "rekord nr "+i+", id: "+ item._id + "<div><h4>"+item.new1+"<br>" +item.new2+"<br>"+item.new3+"</h4><br>";
                    str += "<a href='index.html?" + item._id + "'>Usuń rekord</a>";
                    str += "<br><br><br>---</div>";
					i++;
                });
			db.close();
            });            
        });
    }

    function add_to_DB(new_record) {
        MongoDBClient.connect(db_port, {useNewUrlParser: true, useUnifiedTopology: true}, (err, db) => {
            if (err) throw err;

            const mojaDB = db.db("mojabaza");
			
            mojaDB.collection("input").insertOne(new_record, (err, res) => {
                if (err) throw err;
                db.close();
            });
        });
    }
	
    function delete_from_DB(id_record) {
        MongoDBClient.connect(db_port, (err, db) => {
            if (err) throw err;

            const mojaDB = db.db("mojabaza");

            mojaDB.collection("input").deleteOne({_id: ObjectId(id_record)});

            db.close();
        });
    }

}).listen(server_port);