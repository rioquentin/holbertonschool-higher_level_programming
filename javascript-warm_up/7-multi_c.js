#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let i = 0;
while (i < argv[2]) {
  console.log('C is fun');
  i += 1;
}
