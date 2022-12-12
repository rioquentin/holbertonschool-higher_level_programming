#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const fs = require('fs');
const path = require('path');
try {
  const pathFile = path.resolve(path.dirname(__filename), './' + argv[2]);
  if (fs.existsSync(pathFile)) {
    const input = fs.readFileSync(pathFile, 'utf8');
    console.log(input);
  }
} catch {
  process.exit();
}
