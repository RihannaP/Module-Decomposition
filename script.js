import express from "express"
const app = express();

app.use(express.json());

function usernameExtractor(req, res, next) {
  const username = req.get("X-Username");
  req.username = username ? username : null;
  next();
}

app.post("/", usernameExtractor,(req, res) => {
  const username = req.username;
  const subjects = req.body;

 

  res.send(response);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});