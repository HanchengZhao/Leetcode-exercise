/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    var length = nums.length;
    var jump_len = 0;
    var i = 0;
    for (; i < length && i <= jump_len; i++) {
        jump_len = Math.max(jump_len, nums[i] + i);
    }
    return i == length;
};

console.log(canJump([0]));