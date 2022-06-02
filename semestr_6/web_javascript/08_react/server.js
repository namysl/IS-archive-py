const server_port = 8888;
console.log("Port: " + server_port);

const express = require('express');
const path = require('path');

const db_port = "mongodb://localhost:27017/";  //zmienic adres!!
const DBclient = require('mongodb').MongoClient;
const ObjectId = require('mongodb').ObjectID;
const MongoDBClient = new DBclient(db_port, { useNewUrlParser: true });

const app = express();
app.use(express.json());
app.use(express.static('public'));

MongoDBClient.connect(err => {
    if (err) throw err;
});

app.post('/newpost', (req, ress) => {
    if (!req.body)
        return res.send("!req.body");
    let post = {
        user: req.body.user,
        title: req.body.title,
        body: req.body.body,
        date: new Date(),
    }
    MongoDBClient.db("newmongodb").collection("posts").insertOne(post, (err, res) => {
        if (err) throw err;
        return ress.send("new!");
    })
});

app.get('/getposts', (req, res) => {
    MongoDBClient.db("newmongodb").collection("posts").find({}).toArray((err, result) => {
        if (err) throw err;
        return res.json(result);
    })
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
});

app.listen(server_port);
