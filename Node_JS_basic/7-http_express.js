// import Express (Node library)
const express = require('express');

// create an Express app
const app = express();
//  import async student counter
const countStudents = require('./3-read_file_async');

// define route for GET /
app.get('/', (req, res) => {
  // respond plain text
  res.type('text');
  // send greeting
  res.send('Hello Holberton School!');
});

// route for GET /students
app.get('/students', async (req, res) => {
  res.type('text');
  const path = process.argv[2];

  // capture console.log output
  let output = '';
  // save original console.log
  const originalLog = console.log;

  // override console.log to store logs
  console.log = (msg) => { output += `${msg}\n`; };

  try {
    // run the async student counting function
    await countStudents(path);
    output = output.trimEnd();
    res.send(`This is the list of our students\n${output}`);
    return;
  } catch (err) {
    // restore console.log on error
    console.log = originalLog;
    res.send('This is the list of our students\nCannot load the database');
    return;
  } finally {
    // always restore console.log
    console.log = originalLog;
  }
});

// start server on port 1245
app.listen(1245);
module.exports = app;
