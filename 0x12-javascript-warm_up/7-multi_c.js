#!/usr/bin/node

let arg = parseInt(process.argv[2]);

if (Number.isInteger(arg)) {
  while (arg > 0) {
    console.log('C is fun');
    arg--;
  }
} else {
  console.log('Missing number of occurrences');
}