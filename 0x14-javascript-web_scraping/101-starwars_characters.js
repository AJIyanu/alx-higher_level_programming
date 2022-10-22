#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  const charlist = JSON.parse(response.body).characters;
  // console.log(charlist);
  const dict = {};
  for (const i in charlist) {
    const url = charlist[i];
    // console.log(url);
    dict[url] = work(url);
  }
  console.log(dict);
});

const work = async (url) => {
  await sleep(1000);
  request(url, function (err, resp) {
    if (err) {
      console.error(err);
    }
    return (JSON.parse(resp.body).name);
  });
};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
