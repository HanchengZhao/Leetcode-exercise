/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    //build the hashtable to count the target char occurrance
    var targethash = [];
    var targetsum = 0;
    for(var m = 0; m < t.length; m++) {
        if (targethash[t.charAt(m)] === undefined) {
            targethash[t.charAt(m)] = 1;
        }else{
            targethash[t.charAt(m)]++;
        }
        targetsum++;
    }

    var i = 0;
    var sourcesum = 0;
    var res = Number.MAX_SAFE_INTEGER;
    var minStr = "";
    for(var j = 0; j < s.length; j++) {
        if (targethash[s.charAt(j)] > 0) {
            sourcesum++;
        }
        targethash[s.charAt(j)]--;

        while (sourcesum >= targetsum) {
            if (res >= j - i + 1) {
                res = Math.min(res, j - i + 1);
                minStr = s.substring(i,j+1);
            }
            targethash[s.charAt(i)]++;//recover the char at i
            if (targethash[s.charAt(i)] > 0) {
                sourcesum--;
            }
            i++;
        }
    }
    return minStr;
};

console.log(minWindow("ADOBECODEBANC","ABC"));