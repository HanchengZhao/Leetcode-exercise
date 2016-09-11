/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 * @author HanchengZhao
 */
var removeElement = function(nums, val) {
    var index = nums.indexOf(val); 
    while(index !== -1){
        nums.splice(index, 1);
        index = nums.indexOf(val);
    }
    return nums.length;
};
