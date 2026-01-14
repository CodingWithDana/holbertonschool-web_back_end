const fileSystem = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fileSystem.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      console.log(`Number of students: ${students.length}`);

      const studentByFields = {};
      students.forEach((line) => {
        const columns = line.split(',');
        const firstName = columns[0];
        const fields = columns[columns.length - 1];

        if (!studentByFields[fields]) {
          studentByFields[fields] = [];
        }
        studentByFields[fields].push(firstName);
      });
      for (const field in studentByFields) {
        if (Object.prototype.hasOwnProperty.call(studentByFields, field)) {
          const list = studentByFields[field];
          const count = list.length;
          console.log(`Number of students in ${field}: ${count}. List: ${list.join('')}`);
        }
      }
      resolve();
    });
  });
}
module.exports = countStudents;
