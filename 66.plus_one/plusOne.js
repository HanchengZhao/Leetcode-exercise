/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    var length = digits.length;
    if(digits[length-1] !== 9){
        digits[length-1]++;
        console.log(digits);
        return digits;
    }
    digits[length-1] = 0;
    if(length === 1){
        digits.unshift(1);
        return digits;
    }
    var carry = 1;
    for (var i = length - 2; i >= 0; i--){
        if(digits[i]+carry === 10){
            digits[i] = 0;
            if(i === 0){
                digits.unshift(1);
                return digits;
            }
        }else{
            digits[i] += carry;
            break;
        }
    }
    console.log(digits);
    return digits;
};

plusOne([9]);