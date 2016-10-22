/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    var hashmap = new Map();
    for(var i = 0; i < s.length; i++){
        hashmap.set(s[i], hashmap.get(s[i])+1 || 1);
    }
    for(var j = 0; j < t.length; j++){
        var value = hashmap.get(t[j]);
        if(value){//value == 0 or undefined
            hashmap.set(t[j], --value);
        }else{
            return t[j];
        }
    }
    
};

console.log(findTheDifference('abcde', "abcdel"));