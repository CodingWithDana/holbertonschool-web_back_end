// import Node's built-in file system module so files can be read
const fileSystem = require('fs');

function countStudents(path) {
  // read the file
  let data;
  try {
    data = fileSystem.readFileSync(path, 'utf8');
    // split file into lines
    let lines = data.split('\n');
    lines = lines.filter((line) => line.trim() !== '');
    // remove the first line (the header)
    const students = lines.slice(1);
    // count total students
    const total = students.length;
    console.log(`Number of students: ${total}`);

    // group students by field
    const studentsByFields = {};
    // loop through each student line
    students.forEach((line) => {
      const columns = line.split(', ');
      const firstName = columns[0];
      const fields = columns[columns.length - 1];
      // add student to the correct field
      if (!studentsByFields[fields]) {
        // if it's the first CS student, then create an. array
        studentsByFields[fields] = [];
      }
      // then push their first name into the field group
      studentsByFields[fields].push(firstName);
    });
    // print results per field
    for (const field in studentsByFields) {
      if (Object.prototype.hasOwnProperty.call(studentsByFields, field)) {
        const list = studentsByFields[field];
        const count = list.length;
        console.log(`Number of students in ${field}: ${count}. List: ${list.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
