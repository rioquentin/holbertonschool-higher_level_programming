#!/usr/bin/node
let empty;
class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || h === undefined || w === undefined) {
      this.width = empty;
      this.height = empty;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
