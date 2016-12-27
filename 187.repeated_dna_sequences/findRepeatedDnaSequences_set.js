var findRepeatedDnaSequences = function(s) {
    if(s.length <= 10) return [];
    var result = [];
    var seen = new Set();
    for(var i = 0; i < s.length-9; i++){
        var seq = s.substr(i,10);
        if(seen.has(seq) && result.indexOf(seq) === -1){
            result.push(seq);
        }else{
            seen.add(seq);
        }
    }
    return result;
};

console.log(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));