#!/usr/bin/node
const importDict = require('./101-data');

const _dict = importDict.dict;

const a = [];
const b = [];
const c = [];

for (const key in _dict) {
  if (_dict[key] === 1) {
    a.push(key);
  } else if (_dict[key] === 2) {
    b.push(key);
  } else if (_dict[key] === 3) {
    c.push(key);
  }
}
const newDict = {
  1: a,
  2: b,
  3: c
};
console.log(newDict);
