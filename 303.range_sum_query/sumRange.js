/**
 * @constructor
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    var sum = 0;
    var map = [0];
    for(var i = 1; i <= nums.length; i++){
        sum += nums[i-1];
        map[i] = sum;
    }
    this.map = map;
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    var map = this.map;
    return map[j+1] - map[i];
};


/**
 * Your NumArray object will be instantiated and called as such:
 * var numArray = new NumArray(nums);
 * numArray.sumRange(0, 1);
 * numArray.sumRange(0, 2);
 */
 
 var numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
console.log(numArray.sumRange(0, 2));
console.log(numArray.sumRange(2, 5));
console.log(numArray.sumRange(0, 5));