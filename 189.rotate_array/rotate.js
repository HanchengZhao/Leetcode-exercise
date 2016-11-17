/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    if(k > nums.length){
        k = k % nums.length;
    }
    var rotateArr = nums.slice(nums.length-k);
    var remainingArr = nums.slice(0,nums.length-k);
    nums = rotateArr.concat(remainingArr);
    return nums;
};
console.log(rotate([1,2],1));