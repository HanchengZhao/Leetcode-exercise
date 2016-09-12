/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 * @author HanchengZhao
 */
// var strStr = function(haystack, needle) {
//     return haystack.indexOf(needle);
// }; // easily down with one line built-in function


var strStr = function(haystack, needle) {
    for(var i = 0; i <= haystack.length; i++){
        if(haystack[i]===needle){
            return i;
        }
    }
    return -1;
};