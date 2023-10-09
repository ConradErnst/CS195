const express = require('express');
const app = express();
const port = 3000; // You can change this to your desired port

app.use(express.static('public')); // Serve static files from the "public" directory

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
