#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  const charlist = JSON.parse(response.body).characters;
  // console.log(charlist);
  let names = {};
  for (const i in charlist) {
    const url = charlist[i];
    // console.log(url);
    request(url, function (err, resp) {
      if (err) {
        console.error(err);
      }
      names[i] = JSON.parse(resp.body).name;
    });
  }
  console.log(names);
});
