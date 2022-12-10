#!/usr/bin/node

const process = require('process');
const argv = process.argv;
num = argv[2];

function fac(n) {
  if (n < 0) {
    return -1;
  } else if (n == 0) {
    return 1;
  } else {
    return (n * fac(n - 1));
  }
}

if (isNaN(num)) {
  console.log(1);
} else {
  result = fac(num);
  console.log(result)
}