/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    var myMap = new Map();
    
    for(var i = 0; i < nums.length; ++i){
        
        var compliment = target - nums[i];
        if(myMap.get(compliment) !== undefined){
            console.log([myMap.get(compliment), i]);
            return [myMap.get(compliment), i];
        }
        myMap.set(nums[i], i);// num[i] as key, i as position
    }
    
    
    return false;
};

var nums = [2, 7, 11, 15];
var target = 9;
twoSum(nums, target);

//costs O(n)