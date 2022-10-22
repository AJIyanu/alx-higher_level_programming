#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(response.body).characters;
  characters.forEach((character) => {
    request(character, function (err, response, content) {
      if (!err) {
        console.log(JSON.parse(content).name);
        while (!JSON.parse(content).name) {
          let i = 0;
          i = i + i;
        }
      }
    });
  });
}
);
