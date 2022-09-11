#!!/usr/bin/node

exports.logMe = function (item) {
  let count = 0;
  function dispcount (item) {
    console.log(count + ' : ' + item);
    count += 1;
  }

  dispcount();
};
