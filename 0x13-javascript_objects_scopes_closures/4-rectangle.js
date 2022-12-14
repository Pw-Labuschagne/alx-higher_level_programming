#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    const t = this.width;
    this.width = this.height;
    this.height = t;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    for (let s1 = 0; s1 < this.height; s1++) {
      let txt = '';
      for (let s2 = 0; s2 < this.width; s2++) {
        txt += 'X';
      }
      console.log(txt);
    }
  }
}

module.exports = Rectangle;
