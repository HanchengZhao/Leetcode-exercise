/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    var result = [];
    nums.sort(function(a, b){return a-b});
    for(var i = 0; i < nums.length-2; i++){
        if(i===0 || i!==0 && nums[i]!== nums[i-1]){//the same number can't be the first element again
        var target = 0 - nums[i];
        var lo = i+1;
        var hi = nums.length-1;
        while(lo < hi){
            if(nums[lo]+nums[hi] === target){
                result.push([nums[i],nums[lo],nums[hi]]);
                while(lo < hi && nums[lo] === nums[lo+1]) lo++;//eliminate all the duplicate combinations
                while(lo < hi && nums[hi] === nums[hi-1]) hi--;
                lo++;
                hi--;
            }else if(nums[lo]+nums[hi] < target){
                lo++;
            }else{
                hi--;
            }
        }    
        }
        
    }
    return result;
};
console.log(threeSum([-1, 0, 1, 2, -1, -4]));