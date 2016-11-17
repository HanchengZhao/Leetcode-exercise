/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length === 0) return 0;
    var maxValue = [];
    maxValue[0] = nums[0];
    maxValue[1] = Math.max(nums[1], nums[0]);
    for(var i = 2; i < nums.length; i++){
        maxValue[i] = Math.max(maxValue[i-1], maxValue[i-2] + nums[i]);//take this value or not
    }
    return maxValue[nums.length-1];
};

console.log(rob([1,4,2,8]));