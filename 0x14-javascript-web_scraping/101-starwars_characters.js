#!/usr/bin/node

const request = require('request');
let charlist = [];
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  charlist = JSON.parse(response.body).characters;
  for (let i = 0; i < charlist.length; i++) {
    request(charlist[i], function (err, resp) {
      if (err) {
        console.error(err);
      }
      console.log(JSON.parse(resp.body).name);
    });
  }
});
