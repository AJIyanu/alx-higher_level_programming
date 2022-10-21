#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  let charlist = JSON.parse(response.body).characters;
  console.log(charlist);
  for (const i of charlist) {
    request(charlist[i], function (err, resp) {
      if (err) {
        console.error(err);
      }
      console.log(JSON.parse(resp.body).name, charlist[i]);
    });
  }
});
