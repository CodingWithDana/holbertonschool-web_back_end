// import Node's built-in modules and file
const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

// create server with async handler
const app = http.createServer(async (req, res) => {
  // parse the URL path
  const reqUrl = url.parse(req.url).pathname;
  // route '/'
  if (reqUrl === '/') {
    //  set header
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    // send http response
    res.end('Hello Holberton School!');
  // route '/students'
  } else if (reqUrl === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    // get the file path from command line
    const path = process.argv[2];
    // capture console.log output
    let output = '';
    const originalLog = console.log;
    console.log = (msg) => { output += `${msg}\n`; };
    // call the student counting function
    try {
      await countStudents(path);
    } catch (err) {
      console.log = originalLog;
      res.end('This is the list of our students\nCannot load the database');
      return;
    }
    // restore orginal console.log (note: never leave console.log overidden)
    console.log = originalLog;
    //  trim final new line
    output = output.trimEnd();
    res.end(`This is the list of our students\n${output}`);
  }
});
app.listen(1245);
module.exports = app;
