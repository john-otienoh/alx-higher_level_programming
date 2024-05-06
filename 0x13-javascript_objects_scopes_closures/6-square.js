#!/usr/bin/node

const SquareSix = require('./5-square');
class Square extends SquareSix {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sq = '';
      for (let j = 0; j < this.width; j++) {
        sq += c;
      }
      console.log(sq);
    }
  }
}

module.exports = Square;
