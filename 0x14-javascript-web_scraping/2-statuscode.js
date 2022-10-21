#!/usr/bin/node
// send a get request to a server

const fetch = require('node-fetch')

const arg = process.argv;

function makeRequest () {
  fetch(arg[2])
    .then(response => {
      console.log('response.status: ', response.status);
      console.log(response);
    })
    .catch(err => {
      console.log(err);
    });
}

makeRequest();
