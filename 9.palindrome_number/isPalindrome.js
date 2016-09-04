/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0) return false;
    if(x > Math.pow(2,31)){ //overflow handling
        return false;
    }
    var original = x;
    var length = Math.log(x) * Math.LOG10E + 1 | 0;
    var reverse = 0;
    while (original !== 0){
        var modulus = original % 10;
        original = Math.floor(original / 10);
        reverse += modulus * Math.pow(10, length - 1);
        length--;
    }
    console.log(reverse);
    return (x === reverse) ? true : false ;
 
};

console.log(Math.pow(2,31));

isPalindrome(1);
