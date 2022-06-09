const express = require("express");
const cors = require("cors");

const app = express();

var corsOptions = {
  origin: "http://localhost:8081"  //192.168.14.34
};

app.use(cors(corsOptions));

app.use(express.json());

app.use(express.urlencoded({ extended: true }));

const db = require("./app/models");
db.mongoose
  .connect(db.url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
  })
  .then(() => {
    console.log("połączono z db");
  })
  .catch(err => {
    console.log("błąd połączenia z db", err);
    process.exit();
  });

app.get("/", (req, res) => {
  res.json({ message: "forum połączono" });
});

require("./app/routes/turorial.routes")(app);

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server PORT: ${PORT}.`);
});
