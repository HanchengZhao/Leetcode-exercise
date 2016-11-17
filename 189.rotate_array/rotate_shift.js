var rotate = function(nums, k) {
    while (k > 0) {
        nums.unshift(nums.pop());
        k--;
    }
};
console.log(rotate([1,2,3,4,5,6],13));