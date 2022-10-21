#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  const charlist = JSON.parse(response.body).characters;
  console.log(charlist);
  for (i in charlist) {
    console.log(i);
    request(charlist[i], function (err, resp) {
  for (const i of charlist) {
    let url = charlist[i]
    request(url, function (err, resp) {
      if (err) {
        console.error(err);
      }
      console.log(i, JSON.parse(resp.body).name, charlist[i]);
    });
    console.log(i);
  }
});
