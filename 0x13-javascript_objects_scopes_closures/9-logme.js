#!/usr/bin/node
let NumArgs = 0;
exports.logMe = function (item) {
  console.log(NumArgs + ': ' + item);
  NumArgs++;
};
