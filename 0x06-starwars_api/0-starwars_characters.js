#!/usr/bin/node
var request = require('request')
function get_characters(){
	request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (t, ty)=>{
	var characters = JSON.parse(ty.body).characters;
	for (i=0; i<=characters.length; i++){
		request.get(characters[i], (res, response)=>{
			console.log(JSON.parse(response.body).name);
	})
	}
})}
get_characters()
