#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let i = 2;
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log(argv[i]);
} else {
  while (1) {
    if (argv[i] != undefined){
      console.log(argv[i]);
      i = i + 1;
    } else {
      break;
    }
  }
}
