var plusOne = function(digits) {
    var length = digits.length;
  
    for (var i = length - 1; i >= 0; i--){
        if(digits[i] < 9){
            digits[i]++;
            return digits;
        
        }else{
            digits[i] = 0;
        }
    }
    digits.unshift(1);
    console.log(digits);
    return digits;
};

plusOne([9]);