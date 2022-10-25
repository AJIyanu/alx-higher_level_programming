#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get('http://swapi-api.hbtn.io/api/people', function (err, response) {
  if (!err) {
    const charlist = JSON.parse(response.body).results;
    const chardict = {};
    for (let i = 0; i < charlist.length; i++) {
      chardict[charlist[i].url] = charlist[i].name;
    }
    console.log(chardict);
  }
});
