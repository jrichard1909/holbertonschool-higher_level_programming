#!/usr/bin/node
if (process.argv.slice(2)[0]) {
  console.log(process.argv.slice(2)[0]);
} else {
  console.log('No argument');
}
