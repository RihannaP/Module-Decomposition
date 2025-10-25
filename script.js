import express from "express"
const app = express();

app.use(express.json());

function usernameExtractor(req, res, next) {
  const username = req.get("X-Username");
  req.username = username ? username : null;
  next();
}


const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});