/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    //using a stack to check the order of parentheses
    var parenthesesArray = [];
    var length = s.length;
    for(var i = 0; i < length; i++ ){
        if(s[i] === '(' ) parenthesesArray.push(')');
        if(s[i] === '[' ) parenthesesArray.push(']');
        if(s[i] === '{' ) parenthesesArray.push('}');
        if(s[i] === ')' || s[i] === ']' || s[i] === '}'){
            var sign = parenthesesArray.pop()
            if(s[i] === sign){
                continue;
            }else{
                return false;
            }
        }
    }
    if(parenthesesArray.length === 0){
        return true;
    }else{
        return false;
    }
};