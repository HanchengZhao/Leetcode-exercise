/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    // var bits = parseInt(n.toString(2),2);
    var bits = n;
    // console.log(bits);
    var count = 0;
    while (bits != 0) {
        if (bits & 1) {
            count++;
        }
        bits >>>= 1;//need to use >>> instead of >>     http://www.w3schools.com/js/js_bitwise.asp
    }
    return count;
};

console.log(hammingWeight(2147483648));