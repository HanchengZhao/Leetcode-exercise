/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    if (nums.length === 0) {
        return -1;
    }

    return quickSelect(nums, 0, nums.length-1, k);
};

var quickSelect = function(nums, start, end, k) {
    if(start === end) {
        return nums[start];
    }
    var left = start;
    var right = end;
    var pivot = nums[start + Math.floor(Math.random() * (end - start + 1))];
    while (left <= right) {
        while (left <= right && nums[left] > pivot) {
            left++;
        }

        while (left <= right && nums[right] < pivot) {
            right--;
        }
        //swap
        if (left <= right) {
            var temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
    if (start + k - 1 <= right) {
        return quickSelect(nums, start, right, k);
    }
    if (start + k - 1 >= left) {
        return quickSelect(nums, left, end, k - (left - start));
    }
    return nums[right + 1];
};

console.log(findKthLargest([3,2,1,5,6,4], 6));
console.log(findKthLargest([99, 99], 1));