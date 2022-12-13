#!/usr/bin/node
const request = require('request');
const API_URL = process.argv[2];
const CHARACTER_ID = 18;
function getData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
function characterInFilm (film, characterId) {
  return film.characters.some((characterUrl) => {
    const characterIdRegex = new RegExp(`/${characterId}/$`);
    return characterUrl.match(characterIdRegex);
  });
}
async function main () {
  const filmsData = await getData(API_URL);
  const films = filmsData.results;
  let count = 0;
  films.forEach((film) => {
    if (characterInFilm(film, CHARACTER_ID)) {
      count += 1;
    }
  });
  console.log(count);
}
main();
