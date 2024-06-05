#!/usr/bin/node
const request = require('request');
const optiom = {
	url: process.argv[2];,
	method: 'GET';,
}
request(optiom, function (e, response) {
	console.log(e | 'code: ${response.statuscode}');
});
