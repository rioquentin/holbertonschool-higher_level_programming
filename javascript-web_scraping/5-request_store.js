#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    fs.writeFile(data, process.argv[3], 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
