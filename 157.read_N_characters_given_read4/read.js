/**
 * Definition for read4()
 *
 * @param {character[]} buf Destination buffer
 * @return {number} The number of actual characters read
 * read4 = function(buf) {
 *     ...
 * };
 */

/**
 * @param {function} read4()
 * @return {function}
 */
var solution = function(read4) {
  /**
   * @param {character[]} buf Destination buffer
   * @param {number} n Number of characters to read
   * @return {number} The number of actual characters read
   */
  return function(buf, n) {
    let idx = 0;
    while (n > 0) {
      let buf4 = new Array(4);
      const l = read4(buf4);
      if (l == 0) return idx;
      const range = Math.min(l, n);
      // can't set Math.min(l,n) as the boundary directly in the condition expression
      // because n changes everytime
      for (let i = 0; i < range; i++) {
        buf[idx] = buf4[i];
        idx++;
        n--;
      }
    }
    return idx;
  };
};
