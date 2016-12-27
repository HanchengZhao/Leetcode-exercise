/*jshint curly:true, debug:true */
/**
 * @param {string} str
 * @return {boolean}
 */


var repeatedSubstringPattern = function(str) {
    //substring has to start from the beginning
    var len = str.length;
    for (var i = 1; i < len; i++) {
        var substr = str.substring(0, i);
        // console.log(substr);
        var count = Math.ceil(len / i);
        for (var j = 1; j <= count; j++) {
            // console.log(substr.repeat(j));
            if (substr.repeat(j) === str) return true;
        }
    }
    return false;
};

console.log(repeatedSubstringPattern('bb'));
