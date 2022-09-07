#!/usr/bin/node 

const arg = process.argv;
const len = arg.length;
function secondlarge (l, array) {
  if (l < 4) {
    return (0);
  }
  let large = array[2];
  let lar;
  for (let start = 3; start < l; start++) {
    if (array[start] > large) {
      lar = large;
      large = array[start];
    }
  }
  return (lar);
}
console.log(secondlarge(len, arg));
