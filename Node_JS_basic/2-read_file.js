// import Node's built-in file system module so files can be read
const fileSystem = require('fs');

function countStudents(path) {
  // read the file
  let data;
  try {
    data = fileSystem.readFileSync(path, 'utf8');
    // split file into lines
    const lines = data
      .split('\n')
      .filter((line) => line.trim() !== '');

    // remove the first line (the header)
    const students = lines.slice(1);

    // count total students
    console.log(`Number of students: ${students.length}`);

    // group students by field
    const studentsByFields = {};
    // loop through each student line
    students.forEach((line) => {
      const columns = line.split(',');
      const firstName = columns[0].trim();
      const field = columns[columns.length - 1].trim();
      // add student to the correct field
      if (!studentsByFields[field]) {
        // if it's the first CS student, then create an. array
        studentsByFields[field] = [];
      }
      // then push their first name into the field group
      studentsByFields[field].push(firstName);
    });

    // log results per field
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
