#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let i = 2;
if (argv[2] === undefined) {
  console.log('No argument');

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
