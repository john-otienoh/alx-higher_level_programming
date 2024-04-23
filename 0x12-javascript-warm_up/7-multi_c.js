#!/usr/bin/node
const x = process.argv[2];
for (let i = 0; i < x; i++) {
	if (process.argv.length === 2) {
		console.log("Missing number of occurrences");
	}
	else {
		console.log('C is fun');
	}
}
