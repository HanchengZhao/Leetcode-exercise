/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    var k = n + m - 1;
    var i = m - 1;
    var j = n - 1;
    while(k >= 0){
        if (k === i) {
            return;
        } else if (k === j) {
            nums1[k--] = nums2[j--];
        } else {
            nums1[k--] = nums1[i] > nums2[j] ? nums1[i--] : nums2[j--];
        }
    }
    console.log(nums1);
};

merge([0],0,[1,2,3,4,5],5);