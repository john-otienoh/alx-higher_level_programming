#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;
