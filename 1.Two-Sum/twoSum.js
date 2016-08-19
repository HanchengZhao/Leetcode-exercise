/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    var tempNums = [];
    for (var i = 0; i < nums.length; ++i){
        tempNums[i] = target - nums[i];
    }
    
    for (var j = 0; j < nums.length; ++j){
        for(var k = j + 1; k < tempNums.length; ++k){
            if (nums[j] === tempNums[k]){
                return [j, k];
            }else{
                continue;
            }
        }
    }
    
    return false;
};

//costs O(n^2)