/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var max = nums[0];
    var sum = nums[0];
    for(var i = 1; i < nums.length; i++){
        sum = (sum < 0 ? 0 : sum) + nums[i];
        max = Math.max(max,sum);
    }
    return max;
};

console.log(maxSubArray([1]));