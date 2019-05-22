/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  if (nums.length === 0) {
    return -1;
  }
  var lo = 0;
  var hi = nums.length - 1;
  while (lo < hi) {
    var mid = Math.floor((lo + hi) / 2);
    if (nums[mid] === target) {
      return mid;
    }
    if (nums[lo] <= nums[mid]) {
      // left part is sorted
      if (nums[lo] <= target && nums[mid] > target) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    } else {
      if (nums[mid] < target && nums[hi] >= target) {
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }
  }
  return nums[lo] === target ? lo : -1;
};

console.log(search([1, 3], 3));
