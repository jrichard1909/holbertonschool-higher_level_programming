#!/usr/bin/node
const args = process.argv.slice(2);
if (parseInt(args[0])) {
  for (let i = 0; i < parseInt(args[0]); i++) {
    console.log('X'.repeat(parseInt(args[0])));
  }
} else {
  console.log('Missing size');
}
