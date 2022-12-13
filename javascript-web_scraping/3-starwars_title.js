#!/usr/bin/node
const process = require('process');
const request = require('request');
const _id = process.argv[2];
const _url = 'https://swapi-api.hbtn.io/api/films/' + _id;

request(_url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
