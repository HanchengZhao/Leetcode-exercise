/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    var psort = p.split("").sort().join();
    var len = p.length;
    var result = [];
    for(var i = 0; i <= s.length-len; i++){
        var sub = s.substr(i,len).split("").sort().join();
        if(sub === psort){
            result.push(i);
        }
    }
    return result;
};

console.log(findAnagrams("abab","ab"));