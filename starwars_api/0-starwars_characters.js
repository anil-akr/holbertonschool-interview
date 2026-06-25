#!/usr/bin/node
// Script that prints all characters of a Star Wars movie.
// Usage: ./0-starwars_characters.js <Movie ID>
// Names are printed one per line, in the same order as the
// "characters" list returned by the SWAPI /films/ endpoint.

const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

/**
 * Prints every character name, one per line, keeping the original order.
 *
 * It fetches one character at a time and only requests the next one once
 * the current request is finished. Doing it sequentially guarantees the
 * names stay in the same order as the "characters" list.
 *
 * @param {string[]} characterUrls - SWAPI URLs of the characters to print.
 * @param {number} index - Index of the character currently being fetched.
 */
function printCharacters (characterUrls, index) {
  if (index >= characterUrls.length) {
    return;
  }
  request(characterUrls[index], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }
    const character = JSON.parse(body);
    console.log(character.name);
    printCharacters(characterUrls, index + 1);
  });
}

// Step 1: fetch the film, then print all of its characters in order.
request(filmUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  printCharacters(film.characters, 0);
});
