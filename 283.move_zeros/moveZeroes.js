/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let insertIndex = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[insertIndex] = nums[i]
            insertIndex++
        }
    }
    for (let j = insertIndex; j < nums.length; j++) {
        nums[j] = 0
    }
};