#!/usr/bin/node
const args = process.argv.slice(2);
if (parseInt(args[0])) {
  console.log('My number: ' + parseInt(args[0]));
} else {
  console.log('Not a number');
}
