#!/usr/bin/node
const { run } = require('node:test');
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(response.body).characters;
  characters.forEach((character) => {
    setTimeout(function run (character) {
      request(character, function (err, response) {
        if (!err) {
          console.log(JSON.parse(response.body).name);
        }
      });
    }, 5000);
    run(character);
  });
});
