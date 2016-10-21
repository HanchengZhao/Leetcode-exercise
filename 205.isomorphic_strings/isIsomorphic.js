/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if(s.length !== t.length) return false;
    var hashmap1 = new Map();
    var hashmap2 = new Map();
    for(let i = 0; i<s.length; i++){
        if(!hashmap1.has(s[i])){//check if already has the key
            hashmap1.set(s[i], t[i]);
        }else{
            if(hashmap1.get(s[i]) !== t[i]){
                return false;
            }
        }
        if(!hashmap2.has(t[i])){//check if already has the key
            hashmap2.set(t[i], s[i]);
        }else{
            if(hashmap2.get(t[i]) !== s[i]){
                return false;
            }
        }
    }
    return true;
};