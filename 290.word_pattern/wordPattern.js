/**
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPattern = function(pattern, str) {
    var pArray = pattern.split('');
    var sArray = str.split(" ");
    if(pArray.length !== sArray.length) return false;
    var hashmap1 = new Map();
    var hashmap2 = new Map();
    while(pArray.length !== 0){
        var p = pArray.pop();
        var s = sArray.pop();
        if(hashmap1.has(p)){
            var value1 = hashmap1.get(p);
            if(value1 !== s) return false;
        }
        if(hashmap2.has(s)){
            var value2 = hashmap2.get(s);
            if(value2 !== p) return false;
        }
        hashmap1.set(p,s);
        hashmap2.set(s,p);
    }
    return true;
};

wordPattern("abba","dog cat cat dog");