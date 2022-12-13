#!/usr/bin/node
const argNum = parseInt(process.argv.slice(2)[0]);
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else if (num < 0) {
    return -1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(argNum));
