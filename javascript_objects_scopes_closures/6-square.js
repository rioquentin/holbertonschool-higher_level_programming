#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    super.charPrint(c);
  }
}

module.exports = Square;
