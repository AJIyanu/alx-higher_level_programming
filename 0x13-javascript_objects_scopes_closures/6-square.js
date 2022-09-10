#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      const col = 'X';
    } else {
      const col = c;
    }
    for (let start = 1; start < this.width; start++) {
      if (c === undefined) {
        col += 'X';
      } else {
        col += c;
      }
    }
    for (let row = 0; row < this.height; row++) {
      console.log(col);
    }
  }
}
module.exports = Square;
