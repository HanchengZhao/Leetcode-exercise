/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim();
    var arr = s.split(' ');
    return arr[arr.length - 1].length;
};

lengthOfLastWord(" ");