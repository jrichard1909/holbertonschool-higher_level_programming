#!/usr/bin/node
const args = process.argv.slice(2).map(num => parseInt(num));
const lenArgs = args.length;
if (lenArgs <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => a - b);
  console.log(args[lenArgs - 2]);
}
