/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    var len = nums.length;
    if (len === 0) return 0;
    if (len === 1) return nums[0];
    var maxValue = [];
    //do not use the first element
    maxValue[0] = 0;
    maxValue[1] = nums[1];
    for(var i = 2; i < len; i++){
        maxValue[i] = Math.max(maxValue[i-1], maxValue[i-2] + nums[i]);
    }

    var answer_without_first_elment = maxValue[len-1];
    //include the first element
    maxValue[0] = nums[0];
    maxValue[1] = Math.max(nums[0], nums[1]);
    for(var j = 2; j < len; j++){
        maxValue[j] = Math.max(maxValue[j-1], maxValue[j-2] + nums[j]);
    }
    return Math.max(maxValue[len-2],answer_without_first_elment);//use len-2 to eleminate the last one
};

console.log(rob([1,2,3,4,5,6]));