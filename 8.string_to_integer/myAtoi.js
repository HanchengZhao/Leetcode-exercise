/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    //if parseInt（str）is NaN, then return 0
    // using js api parseInt
return Math.max(Math.min(Math.pow(2,31)-1,parseInt(str)?parseInt(str):0),-1*Math.pow(2,31));
};

var strToInt = (str) => {
    let index = 0, sign = 1, total = 0;
    // check empty
    if (str.length === 0) {
        return 0;
    }
    // remove whitespace
    while (index < str.length && str[index] === " ") {
        index++;
    }
    // check the sign
    if (str[index] === "+" || str[index] === "-") {
        sign = str[index] === "+" ? 1 : -1;
        index++;
    }
    // check valid str and avoid overflow   
    const maxInt = Math.pow(2, 31) - 1;
    const minInt = -Math.pow(2, 31);
    while (index < str.length) {       
        let num = str.charCodeAt(index) - "0".charCodeAt(0);
        if (num < 0 || num > 9) {
            break; //throw "this is not a valid number"
        }
        total = total * 10 + num;
        if (total > maxInt || total < minInt) {
            return sign === 1 ? maxInt : minInt
        }
        index++;
    }
    return total * sign;
}

console.log(strToInt("-23413"))