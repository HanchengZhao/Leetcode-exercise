/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    var lower = s.toLowerCase();
    var left = 0;
    var right = s.length-1;
    while (left < right) {
        while(left < right && !lower[left].match(/[0-9a-z]/i)) {
            left++;
        }
        while(left < right && !lower[right].match(/[0-9a-z]/i)) {
            right--;
        }
        if (lower[left] !== lower[right]) {
            return false;
        }else {
            left++;
            right--;
        }
    }
    return true;
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("race a car"));