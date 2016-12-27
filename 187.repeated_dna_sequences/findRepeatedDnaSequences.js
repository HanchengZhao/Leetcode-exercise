/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    if(s.length <= 10) return [];
    var result = [];
    var seq;
    var remaining = s;
    for(var i = 0; i < s.length-10; i++){
        seq = remaining.substr(0,10);
        remaining = remaining.substring(1);
        if(remaining.indexOf(seq) !== -1 && result.indexOf(seq) === -1){//exists in the remaining but remove duplicates
            result.push(seq);
        }
    }
    return result;
};
