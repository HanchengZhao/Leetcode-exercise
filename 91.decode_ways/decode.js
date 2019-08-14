/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if(s.length === 0 || s[0] === "0") {
       return 0;
    }
    var memo = new Array(s.length+1).fill(0);
    memo[0] = memo[1] = 1;
    for(var i = 1; i < s.length; i++) {      
        if(s[i] === "0") {
            if(s[i-1] === "1" || s[i-1] === "2") {
               memo[i+1] = memo[i-1] // only have 1 option
            } else {
                return 0;
            }
        }else if (s[i-1] !== "0" && parseInt(s.slice(i-1,i+1)) <= 26) {
            memo[i+1] = memo[i-1] + memo[i];
        } else {
            memo[i+1] = memo[i]      
        }
    }
    return memo[s.length]
};

numDecodings("1234")