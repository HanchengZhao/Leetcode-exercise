/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k % nums.length;
    var count = 0;
    for (var start = 0; count < nums.length; start++){
        var current = start;
        var prev = nums[start];
        do {
            var next = (current + k) % nums.length;
            var temp = nums[next];
            nums[next] = prev;
            prev = temp;
            current = next;
            count++;
        }while (start != current);
    }
};