/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    var a_arr = a.split('');
    var b_arr = b.split('');
    var c_arr = [];
    var carry = 0;
    while(a_arr.length !==0 && b_arr.length !==0){
        var a_b = Number(a_arr.pop());
        var b_b = Number(b_arr.pop());
        var c = (a_b + b_b + carry) % 2;
        carry = ((a_b + b_b + carry) > 1) ? 1 : 0;
        console.log(carry);
        c_arr.unshift(c);
    }
    var remainArray = (a_arr.length === 0) ? b_arr : a_arr;
    console.log(remainArray);
    
    if(carry > 0){
        for(var i = remainArray.length - 1; i>=0; i--){
            if((Number(remainArray[i]) + carry) <= 1){
                remainArray[i] = Number(remainArray[i]) + carry;
                carry = 0;
                break;
            }
            remainArray[i] = 0;
        }
        if(carry > 0) remainArray.unshift(1);
    }
    var result = remainArray.concat(c_arr);
    console.log(result.join(""));
    return result.join("");
};

addBinary('0','1');