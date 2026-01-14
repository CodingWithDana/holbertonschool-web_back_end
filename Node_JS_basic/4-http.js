// this task is to create a simple web server in Nodejs
// import Node's built-in HTTP module
const http = require('http');
// create HTTP server
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
});
app.listen(1245);
module.exports = app;
