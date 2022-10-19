// interact with a file
// print out the text in utf8
// print error if error

const fs = require('fs');

fs.readFile('input.txt', 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
