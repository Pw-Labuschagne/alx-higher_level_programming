#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const c = parseInt(process.argv[2]);
  let string = '';
  for (let x = 0; x < c; x++) {
    string += 'X';
  }
  for (let i = 0; i < c; i++) {
    console.log(string);
  }
}
