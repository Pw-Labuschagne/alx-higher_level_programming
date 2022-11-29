#!/usr/bin/node

exports.esrever = function (list) {
  let LenList = list.length - 1;
  let c = 0;

  while ((LenList - c) > 0) {
    const temp = list[LenList];
    list[LenList] = list[c];
    list[c] = temp;
    LenList--;
    c++;
  }
  return list;
};
