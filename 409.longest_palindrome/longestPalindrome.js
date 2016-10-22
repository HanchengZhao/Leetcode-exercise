/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    var hashmap = new Map();
    for(var i =0; i < s.length; i++){
        hashmap.set(s[i], hashmap.get(s[i])+1 || 1);
    }
    var length = 0;
    var hasOdd = false;
    hashmap.forEach(function(value){
        if(value % 2 ===0){
            length += value;
        }else{
            hasOdd = true;
            length += value-1;
        }
    });
    return hasOdd === true ? length+1 : length;
};

console.log(longestPalindrome("abccccdd"));