/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    var steps = [];
    steps[0] = 1;
    steps[1] = 2;
    for(var i = 2; i < n; ++i){
        steps[i] = steps[i-2] + steps[i-1];
    }
    return steps[n-1];
};