#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get('http://swapi-api.hbtn.io/api/people', function (err, response) {
  if (!err) {
    let charlist = JSON.parse(response.body).results;
    const chardict = {};
    for (let i = 0; i < charlist.length; i++) {
      chardict[charlist[i].url] = charlist[i].name;
    }
    for (let page = 2; page < 10; page++) {
      request.get('http://swapi-api.hbtn.io/api/people/?page=' + page, function (err, response) {
        if (!err) {
          charlist = JSON.parse(response.body).results;
          for (let i = 0; i < charlist.length; i++) {
            chardict[charlist[i].url] = charlist[i].name;
          }
          console.log(chardict);
          console.log(chardict.length);
        }
      });
    // console.log(chardict);
    // console.log(chardict.length);
    }
  }
});
