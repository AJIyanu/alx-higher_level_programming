#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get('http://swapi-api.hbtn.io/api/people', function (err, response) {
  if (!err) {
    const charlist = JSON.parse(response.body).result;
    console.log(charlist);
  }
});
