/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    var min =Math.abs(nums[0] + nums[1] + nums[2] - target);//initialize
    var result = nums[0] + nums[1] + nums[2];
    nums.sort(function(a, b){return a-b});
    for(var i = 0; i < nums.length-2; i++){
        var sum = 0;
        sum += nums[i];
        var lo = i+1;
        var hi = nums.length-1;
        while(lo < hi){
            if(sum + nums[lo] + nums[hi] === target) return target;
            if(sum + nums[lo] + nums[hi] < target){
                if(Math.abs(sum + nums[lo] + nums[hi] - target) < min){
                    result = sum + nums[lo] + nums[hi];
                    min = Math.abs(sum + nums[lo] + nums[hi] - target);
                }
                lo++;
                
            }else{
                if(Math.abs(sum + nums[lo] + nums[hi] - target) < min){
                    result = sum + nums[lo] + nums[hi];
                    min = Math.abs(sum + nums[lo] + nums[hi] - target);
                }
                hi--;
               
            } 
        }
    }
    return result;
};

console.log(threeSumClosest([-1,-5,-3,-4,2,-2],
0));