/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    var loopArray = [];
    while(n !== 1){
        if(loopArray.indexOf(n) !== -1) return false;
        loopArray.push(n);
        var sum = 0;
        while(n !== 0){
            var num = n % 10;
            sum += Math.pow(num, 2);
            n = Math.floor(n / 10);
        }
        console.log(sum);
        n = sum;
    }
    return true;
};

console.log(isHappy(7));
