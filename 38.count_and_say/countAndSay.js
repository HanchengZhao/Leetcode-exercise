/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if(n === 1) return '1';
    var str = '1';
    var nth = ''
    for(var j = 1; j < n; j++){
        nth = generateNext(str);
        str = nth;
    }
    return nth;
};

var generateNext = function(string){
    var result = '';
    var count = 1;
    for(var i = 0; i < string.length; i++){
        var pointer = string[i]; // point to current character
        if(string[i] === string[i + 1]){
            count++;
        }else{
            result += count + pointer;
            count = 1;
        }
    }
    return result;
}