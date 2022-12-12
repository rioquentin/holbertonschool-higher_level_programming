#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const fs = require('fs');
const path = require('path');
const pathFile = path.resolve(path.dirname(__filename), './' + argv[2]);
fs.readFile(pathFile, function (err, contents) {
  if (!err) {
    console.log(contents.toString().trim());
  } else {
    console.log(err);
  }
});
