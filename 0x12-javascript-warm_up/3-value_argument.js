#!/usr/bin/node
const { argv } = require('node:process');
if (argv)
	console.log("No argument");
else
	console,.log(`${argv[1]}`);
