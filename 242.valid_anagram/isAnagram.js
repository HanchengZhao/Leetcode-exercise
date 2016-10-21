/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    var s1 = s.split('').sort().join();
    var t1 = t.split('').sort().join();
    if(s1 === t1){
        return true;
    }else{
        return false;
    }
};