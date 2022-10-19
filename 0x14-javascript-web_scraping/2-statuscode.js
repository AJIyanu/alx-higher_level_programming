#!/usr/bin/node
// send a get request to a server

const arg = process.argv;
const req = new XMLHttpRequest();

req.open('GET', arg[2], false);
req.send();
const result = req.responseText;
console('code: ' + result);
