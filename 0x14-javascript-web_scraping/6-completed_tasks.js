#!/usr/bin/node
// count number of completed task
// code written by me gangan

const request = require('request');

request(process.argv[2], function(error, response) {
  if (error) {
    console.error(error);
  }
  let dict = {};
  const allbdy = JSON.parse(response.body);
  console.log(allbdy[0]);
}
);
