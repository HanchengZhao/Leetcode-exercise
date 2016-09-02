/**
 * @param {number} x
 * @return {number}
 */
var reversePositive = function(x){
    var str = x.toString();
    var num = str.split('').reverse().join('');
    return parseInt(num);
}
var reverse = function(x) {
    if(x >= 0){
        var rev = reversePositive(x);
    }else{
        var rev = -reversePositive(x);
    }
    if(rev > Math.pow(2,31) || rev < -Math.pow(2,31)){ //overflow handling
        return 0;
    }else{
        return rev;
    }
};
// console.log(Math.pow(2,31));
// var i = reverse(-123);
// console.log(i)