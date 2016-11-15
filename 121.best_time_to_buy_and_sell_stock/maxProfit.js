/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length === 0 || prices.length === 1) return 0;
    var maxNum = prices[prices.length-1];
    var maxValue = 0;
    for(var i = prices.length-2; i >=0; i--){
        maxValue = Math.max(maxValue,(maxNum - prices[i]));
        maxNum = Math.max(maxNum, prices[i]);
    }
    return maxValue;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));