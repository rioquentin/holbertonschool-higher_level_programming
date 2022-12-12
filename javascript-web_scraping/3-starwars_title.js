#!/usr/bin/node
const process = require('process');
const request = require('request');

const id = process.argv[2]; // the id of the film you want to retrieve

request(`https://swapi.dev/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
