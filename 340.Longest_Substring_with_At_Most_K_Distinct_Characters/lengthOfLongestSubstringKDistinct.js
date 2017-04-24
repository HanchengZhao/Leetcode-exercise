/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var lengthOfLongestSubstringKDistinct = function(s, k) {
    var map = new Map();
    var low = 0;
    var len = 0;
    for(var i = 0; i < s.length; i++){
        map.set(s[i], i);
        if (map.size > k) {
            var smallest = Number.MAX_SAFE_INTEGER;
            //get the smallest value
            for (var value of map.values()) {
              smallest = Math.min(smallest, value);
            }
            low = smallest;
            map.delete(s[low]);
            low++;
        }
        len = Math.max(len, i - low + 1);
    }
    return len;
};

console.log(lengthOfLongestSubstringKDistinct("eceba",2));