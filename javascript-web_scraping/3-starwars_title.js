#!/usr/bin/node
const process = require('process');
const request = require('request');
let id = process.argv[2];

const idFilm = id + "/"; // the id of the film you want to retrieve
request(`https://swapi.dev/api/films/${idFilm}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
