#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurences = 0;
  for (let m = 0; m < list.length; m++) {
    if (searchElement === list[m]) {
      nOccurences++;
    }
  }
  return nOccurences;
};
