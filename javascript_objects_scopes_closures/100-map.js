#!/usr/bin/node
import { list } from './100-data';

const map = list.map((value, index) => value * index);
console.log(list);
console.log(map);
