#!/usr/bin/node
// count number of completed task
// code written by me gangan

const request = require('request');

request(process.argv[2], function(error, body) {
  if (error) {
    console.error(error);
  }
  let dict = {};
  const allbdy = JSON.parse(body.body);
  console.log(allbdy);
}
);
