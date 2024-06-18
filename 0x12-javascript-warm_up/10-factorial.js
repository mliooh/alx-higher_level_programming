#!/usr/bin/node

function factorial (num) {
    if (num === 0 || isNaN(num)) {
      return 1;
    } else {
      return num * factorial(num - 1);
    }
  }
  
  const num = parseInt(process.argv[2]);
  
  const result = factorial(num);
  console.log(result);