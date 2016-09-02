/**
 * @param {string} s
 * @return {string}
 */
function reverseString(s){
    return s.split('').reverse().join(''); //only array in js can be reversed
}
var longestPalindrome = function(s) {
    var length = s.length;
    var str = '';
    var longestPalin = '';
    for(var i = 0; i < length; i++){
        for(var j = i + 1; j <= length; j++){ //j <= length
            str = s.substring(i,j);
            var rev = reverseString(str);
            if(str === rev){
                if(str.length > longestPalin.length){
                    longestPalin = str;
                }
            }
        }
    }
    return longestPalin;
};//takes O(n^2);

// var a = "abcbafasdf";
// longestPalindrome(a);