/**
 * @param {string} str
 * @return {boolean}
 */

var repeatedSubstringPattern = function(str) {
    var len = str.length;
    if(len <= 1) return false;
    for(var i = Math.ceil(len/2); i >= 1; i--){
        if(len % i === 0){
            var m = len / i;
            var sub = str.substr(0,i);
            // console.log(sub);
            if(sub.repeat(m) === str){
                return true;
            }
        }
    }
    return false;
};


console.log(repeatedSubstringPattern("aaaaaaaaaaaaaaaaaaaaa"));
console.log(repeatedSubstringPattern('bb'));
console.log(repeatedSubstringPattern('abaababaab'));



