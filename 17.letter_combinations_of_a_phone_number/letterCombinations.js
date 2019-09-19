/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
  if (digits === "") return [];
  const map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
  };
  let res = [""];
  for (let digit of digits) {
    let temp = [];
    for (let char of map[digit]) {
      for (let last of res) {
        temp.push(last + char);
      }
    }
    res = temp.slice();
  }
  return res;
};
