#!/usr/bin/node

const args = process.argv.slice(2);

const integers = args.map(arg => parseInt(arg)).sort((a, b) => b - a);

if (integers.length < 2) {
  console.log(0);
} else {
  let secondBiggest = integers[1];
  for (let i = 2; i < integers.length; i++) {
    if (integers[i] < secondBiggest) {
      break;
    }
    secondBiggest = integers[i];
  }
  console.log(secondBiggest);
}