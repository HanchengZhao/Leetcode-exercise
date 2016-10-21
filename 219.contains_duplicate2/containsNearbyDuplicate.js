/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    var hashmap = new Map();
    for(var i = 0; i < nums.length; i++){
        if(hashmap.has(nums[i])){
            var value = hashmap.get(nums[i]);
            if(Math.abs(value - i) <= k) return true;
            hashmap.set(nums[i], i);//replace the original duplicate
        }else{
            hashmap.set(nums[i], i);
        }
    }
    return false;
};