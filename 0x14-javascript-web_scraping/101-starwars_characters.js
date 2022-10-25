#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response) {
  if (!err) {
    const charlist = JSON.parse(response.body).characters;
    console.log(charlist);
  }
});
