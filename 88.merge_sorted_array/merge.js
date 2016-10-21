/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    var i = 0, j = 0;
    while(i < m && j < m){
        if (nums1[i] >= nums2[j]){
            nums1.splice(i,0,nums2[j]);//start, deleteCount, addItem
            j++;
        }else{
            i++;
        }
    }
    if(i === m){
        
        nums1 = nums1.concat(nums2.slice(j, n));
    }
    console.log(nums1);
};

merge([0],0,[1,2,3,4,5],5);