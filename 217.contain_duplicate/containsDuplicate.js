/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var set1 = new Set();
    for(var i = 0; i < nums.length; i++){
      if(set1.has(nums[i])){
        return true;  
      }else{
          set1.add(nums[i]);
      }
    }
    return false;
};