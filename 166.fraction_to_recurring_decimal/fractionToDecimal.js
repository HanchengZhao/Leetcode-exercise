/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    if(numerator === 0) return "0";
    var result = "";
    
    if(numerator < 0 ^ denominator < 0){//determine the sign
        result += "-";
    }
    var n = Math.abs(numerator);
    var d = Math.abs(denominator);
    result += (Math.floor(n / d));//integal part
    n %= d;
    if(n !== 0){//fraction part
        result += ".";
        var repeatingPattern = new Map();
        while (n !== 0){
            n *= 10;
            var remainder = Math.floor(n / d);
            if(repeatingPattern.has(n)){//same numerator occurs
                var index = repeatingPattern.get(n);
                var tempArr = result.split("");
                tempArr.splice(index,0,"(");
                tempArr.push(")");
                return tempArr.join("");
            }else{
                repeatingPattern.set(n, result.length);
                result += remainder;
                n %= d;
            }
            
        }
    }

    return result;
};
console.log(fractionToDecimal(1,2));
console.log(fractionToDecimal(2,1));
console.log(fractionToDecimal(2,3));
console.log(fractionToDecimal(1,6));
console.log(fractionToDecimal(1,99));
console.log(fractionToDecimal(1,9999));
console.log(fractionToDecimal(100,33));


    
    // while(numerator !== 0){
    //     if(numerator < denominator){
    //         if(result === ""){//initial situation
    //             result += "0.";
    //         }else if(result.indexOf(".") === -1){//no fraction part yet
    //             result += ".";
    //         }else{
                
    //             result += "0";
    //         }
    //     }else{
    //         var num = Math.floor(numerator / denominator);//int part
    //         result += num;
    //         numerator %= denominator; //mod
    //         if(!repeatingPattern.has(numerator)){//is repeating
    //             repeatingPattern.set(numerator, result.length);
    //         }else{
    //             var index = repeatingPattern.get(numerator);
    //             var tempArr = result.split("");
    //             tempArr.splice(index,0,"(");
    //             tempArr.push(")");
    //             return tempArr.join("");
    //         }
            
    //     }
    //     numerator *= 10;
    // }