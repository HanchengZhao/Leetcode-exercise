var intersect = function(nums1, nums2) {
    var result = [];
    var shortArray = nums1.length > nums2.length ? nums2 : nums1;
    var longArray = nums1.length > nums2.length ? nums1 : nums2;
    
    for(var i = 0; i < shortArray.length; i++){
        var value = shortArray[i];
        if(longArray.indexOf(value) !== -1){
            var index = longArray.indexOf(value);
            longArray.splice(index,1);
            result.push(value);
        }
    }
    
    return result;
};

console.log(intersect([1,2,2,1],[2,2]));