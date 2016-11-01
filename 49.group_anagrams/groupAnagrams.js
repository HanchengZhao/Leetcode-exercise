/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    // var sorted = {};
    var table = new Map();
    var result = [];
    for(var i = 0; i < strs.length; i++){
        var str = strs[i].split("").sort().join("");
        if(!table.get(str)){
            table.set(str,[strs[i]]);
        }else{
            var arr = table.get(str);
            arr.push(strs[i]);
            table.set(str,arr);
        }
    }
    for(let [key, value] of table){
        result.push(value);
    }
    return result;
    
};