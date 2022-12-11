#!/usr/bin/node
const importArray = require('./100-data');

const listed = importArray.list;
const mapped = listed.map((value, index) => value * index);
console.log(listed);
console.log(mapped);
