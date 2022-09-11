#!!/usr/bin/node

exports.logMe = function (item) {
  let count = 0;
  function dispcount (itemm) {
    console.log(count + ' : ' + itemm);
    count += 1;
  }

  return (dispcount(item));
};
