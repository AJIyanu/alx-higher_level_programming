#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request.get(url, function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (err, response, content) {
        if (!err) {
          console.log(JSON.parse(content).name);
        }
      });
    });
  }
});
