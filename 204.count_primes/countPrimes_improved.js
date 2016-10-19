/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    var notPrime = new Array(n);
    for(var i = 2; i < Math.sqrt(n); i++){//only need to test under n^2
        if(notPrime[i] !== true){
            for(var j =2; j*i < n; j++){//eliminate the possiblilities
                notPrime[i*j] = true;
            }
        }
    }
    var count = 0;
    for(let i = 2; i < n; i++){
        if(notPrime[i] !== true) count++;
    }
    return count;
};



console.log(countPrimes(40000));

