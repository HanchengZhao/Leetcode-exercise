/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    var result = [];
    var shortArray = nums1.length > nums2.length ? nums2 : nums1;
    var longArray = nums1.length > nums2.length ? nums1 : nums2;
    
    for(var i = 0; i < shortArray.length; i++){
        var value = shortArray[i];
        if(longArray.indexOf(value) !== -1 && result.indexOf(value) === -1){
            result.push(value);
        }
    }
    
    return result;
};