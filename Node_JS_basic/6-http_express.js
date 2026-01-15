const express = require('express');

// express() creates the server
const app = express();

// define the route for '/'
app.get('/', (req, res) => {
  //  send 'Hello' as the body
  res.send('Hello Holberton School!');
});

// start the server
app.listen(1245);

module.exports = app;
