/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var str = '';
    var max = 0;
    for(var i = 0; i < s.length; i++){
        var pos = str.indexOf(s[i]);
        if( pos != -1){
            max = Math.max(max, str.length);
            str = str.substring(pos+1);
        }
       str = str + s[i]; //this charater has to be added anyway
        
    }
    max = Math.max(max, str.length);
    return max;
};