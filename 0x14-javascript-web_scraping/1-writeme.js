#!/usr/bin/node
// interact with a file
// print out the text in utf8
// print error if error

const arg = process.argv;
const fs = require('fs');

fs.writeFile(arg[2], arg[3], (err, data) => {
  if (err) throw err;
  console.log(data);
});
