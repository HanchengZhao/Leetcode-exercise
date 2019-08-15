/**
 * @param {number} num
 * @return {string}
 *
 * Input: 1234567891
 * Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 */
var numberToWords = function(num) {
  if (num === 0) return "Zero";
  const underTwenty = `One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen`.split(
    " "
  );
  const tens = "Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(
    " "
  );
  // put a space at the beginning is a trick to handle numbers < 1000
  const thousands = " Thousand Million Billion".split(" ");

  let word = "";
  function helper(num) {
    // num should be under 1000 or bigger than 0
    if (num >= 1000 || num <= 0) {
      return "";
    }
    // under twenty
    if (num < 20) {
      return underTwenty[num - 1] + " ";
    } else if (num < 100) {
      return tens[Math.floor(num / 10) - 1] + " " + helper(num % 10);
    } else {
      // 100 <= number < 1000
      return (
        underTwenty[Math.floor(num / 100) - 1] + " Hundred " + helper(num % 100)
      );
    }
  }
  let i = 0;
  while (num > 0) {
    console.log(num);
    if (num % 1000 > 0) {
      // start from the least significant digit
      word = helper(num % 1000) + thousands[i] + " " + word;
    }
    i++;
    num = Math.floor(num / 1000);
  }

  return word.trim();
};

let res = numberToWords(20);
console.log(res);
