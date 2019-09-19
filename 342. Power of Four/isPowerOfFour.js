/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function(num) {
  // should be power of 2
  // but 1 should not appear on odd bit of index
  return num > 0 && (num & (num - 1)) === 0 && (num & 0xaaaaaaaa) === 0;
};
