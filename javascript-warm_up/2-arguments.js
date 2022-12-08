#!/usr/bin/node
const process = require('process');
let argv = process.argv
if (argv.length == 2){
    console.log('No argument')
} else {
    console.log('Argument found')
}
