#!/usr/bin/node

const process = require('process');
const argv = process.argv;

if (isNaN(argv[2]) || isNaN(argv[3]) || argv[2] === undefined) {
  console.log('NaN');
  process.exit(0);
}

add(argv[2], argv[3]);
function add (a, b) {
  const result = parseInt(a, 10) + parseInt(b, 10);
  console.log(result);
}
