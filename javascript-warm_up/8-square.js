#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let i = 0;
let x = 0;

if (isNaN(argv[2])) {
  console.log('Missing size');
  process.exit(0);
} else {
  while (i < argv[2]) {
    x = 0;
    while (x < argv[2]) {
      process.stdout.write('X');
      x += 1;
    }
    console.log('');
    i += 1;
  }
}
