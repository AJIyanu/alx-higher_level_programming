#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get('http://swapi-api.hbtn.io/api/people', function (err, response) {
  if (!err) {
    const charlist = JSON.parse(response.body).results;
    const chardict = {};
    for (let i = 0; i < charlist.length; i++) {
      console.log(charlist[i].name, charlist[i].url);
    }
    // console.log(charlist);
  }
});
