#!/usr/bin/node
const request = require('request');
let index = 0;
let characterz = [];
function GetPerson (character) {
  request.get(character, (error, res, body) => {
    if (error) {
      console.log('wer');
      GetPerson(character);
    } else {
      console.log(JSON.parse(res.body).name);
      index = index + 1;
      if (index < characterz.length) {
        GetPerson(characterz[index]);
      }
    }
  });
}
function GetCharacters () {
  request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (t, ty) => {
    characterz = JSON.parse(ty.body).characters;
    GetPerson(characterz[0]);
  });
}
GetCharacters();
