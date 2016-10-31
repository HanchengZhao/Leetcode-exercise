/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    var table = [];
    var result = [];
    for(var i = 0; i < 26; i++){//initialize
        table[i] = 0;
    }
    for(i = 0; i< p.length; i++){
        table[p.charCodeAt(i) - "a".charCodeAt(0)]++;//set the table
    }
    for(var j = 0; j <= s.length-p.length; j++){
        var isAnagram = true;
        var sub = s.substr(j,p.length);
        var table_copy = table.slice();//copy the table
        for(var k = 0; k < sub.length; k++){
            table_copy[sub.charCodeAt(k) - "a".charCodeAt(0)]--;
            if((table_copy[sub.charCodeAt(k) - "a".charCodeAt(0)] < 0)){
                isAnagram = false;
            }
        }
        if(isAnagram){
            result.push(j);
        }
        
    }
    return result;
    
};
console.log(findAnagrams("abab","ab"));