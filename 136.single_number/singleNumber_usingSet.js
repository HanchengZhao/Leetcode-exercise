/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var myset = new Set();
    nums.forEach(function(int){
        if(!myset.has(int)){
            myset.add(int);
        }else{
            myset.delete(int);
        }
    });
    return myset.values().next().value;
};