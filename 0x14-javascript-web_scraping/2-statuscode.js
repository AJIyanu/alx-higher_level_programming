#!/usr/bin/node
// send a get request to a server

const fetch = require('node-fetch')

const arg = process.argv;

function makeRequest () {
  fetch(arg[2])
    .then(response => {
      console.log('code: ', response.status);
    })
    .catch(err => {
      console.log(err);
    });
}

makeRequest();
