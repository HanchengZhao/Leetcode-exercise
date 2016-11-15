/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length === 0 || prices.length === 1) return 0;
    var ans = 0;
    var bought = prices[0];
    for(var i = 1; i < prices.length; i++){
        if(prices[i] > bought){
            if(ans<(prices[i]-bought)){
                ans = prices[i]-bought;
            }
        }else{
            bought = prices[i];
        }
    }
    return ans;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));