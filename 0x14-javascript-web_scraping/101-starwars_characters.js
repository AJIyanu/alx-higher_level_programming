#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  const charlist = JSON.parse(response.body).characters;
  // console.log(charlist);
  for (const i in charlist) {
    const url = charlist[i];
    // console.log(url);
    setTimeout(request(url, function (err, resp, names) {
      if (err) {
        console.error(err);
      }
      console.lo(JSON.parse(resp.body).name);
    }), 2000);
  }
});
