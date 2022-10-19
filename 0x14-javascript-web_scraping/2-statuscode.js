#!/usr/bin/node
// send a get request to a server

const arg = process.argv;

fetch(arg[2])
  .then(response => {
    console.log('code: ' + response.status)
  });
