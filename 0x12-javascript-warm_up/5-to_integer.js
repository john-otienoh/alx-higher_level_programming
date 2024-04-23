#!/usr/bin/node
if (process.argv.length === 2 || typeof Number(process.argv[2]) !== 'string') {
	console.log('Not a number');
}
else {
	console.log('My number: ', parseInt(process.argv[2]));
}
