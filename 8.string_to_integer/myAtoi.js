/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    //if parseInt（str）is NaN, then return 0
return Math.max(Math.min(Math.pow(2,31)-1,parseInt(str)?parseInt(str):0),-1*Math.pow(2,31));
};