/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    var result = [];
    nums.sort(function(a, b){return a-b});
     for(var i = 0; i < nums.length-3; i++){
        if(i===0 || i!==0 && nums[i]!== nums[i-1]){//the same number can't be the first element again
        for(var j = i+1; j < nums.length-2; j++){
            if(j === i+1 ||nums[j] !== nums[j-1]){//unless j is right after i, the same number can't be the second number again
            var tar = target - nums[i] - nums[j];
            var lo = j+1;
            var hi = nums.length-1;
            while(lo < hi){
                if(nums[lo]+nums[hi] === tar){
                    result.push([nums[i],nums[j],nums[lo],nums[hi]]);
                    while(lo < hi && nums[lo] === nums[lo+1]) lo++;//eliminate all the duplicate combinations
                    while(lo < hi && nums[hi] === nums[hi-1]) hi--;
                    lo++;
                    hi--;
                }else if(nums[lo]+nums[hi] < tar){
                    lo++;
                }else{
                    hi--;
                }
            }
            }
        }
        }
        
    }
    return result;
};

console.log(fourSum([0,0,0,0], 0));