#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let s1 = 0; s1 < this.height; s1++) {
      let txt = '';
      for (let s2 = 0; s2 < this.width; s2++) {
        txt += c;
      }
      console.log(txt);
    }
  }
}

module.exports = Square;
