/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    var number = 0;
    for(var j = n-1; j >0; j--){
       if(isPrime(j)) number++;
    }
    
    return number;
};

var isPrime = function(n) {
    var num = 0;
    for(var i = n; i >= 1; i--){
        if(n % i === 0){
            num++;
        }
    }
    if(num === 2){
        return true;
    }else{
        return false;
    }
};

console.log(countPrimes(100));

