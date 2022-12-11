#!/usr/bin/node
const Square_1 = require('./5-square');

class Square extends Square_1 {
  constructor(s) {
    super(s);
  }
  charPrint(c) {
    super.charPrint(c);
  }
}

module.exports = Square;