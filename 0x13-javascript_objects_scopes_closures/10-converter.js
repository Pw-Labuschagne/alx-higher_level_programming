#!/usr/bin/node

exports.converter = function (base) {
  return function (Numbers) {
    return Numbers.toString(base);
  };
};
