#!!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  function dispcount (itemm) {
    console.log(count + ' : ' + itemm);
    count += 1;
  }

  return (dispcount(item));
};
