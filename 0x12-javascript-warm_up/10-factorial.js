#!/usr/bin/node
function factorial (x) {
  if (x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
if (process.argv[2] === undefined) {
  console.log('1');
} else {
  console.log(factorial(Number(process.argv[2])));
}
