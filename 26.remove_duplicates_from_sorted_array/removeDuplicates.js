/**
 * @param {number[]} nums
 * @return {number}
 * @author HanchengZhao
 *
 */
var removeDuplicates = function(nums) {
    var dummy = nums[0];
    var j = 1;
    var i;
    function recursion(j){//use recursion instead of forloop to avoid index change after removing the num[i]
        for( i = j; i < nums.length; i++){
            if(nums[i] === dummy){
                nums.splice(i, 1);
                 j = i
                recursion(j);
            }else{
                dummy = nums[i];
            };
        }
    };
    recursion(j);
    console.log(nums);
    return nums.length;
};
//needs to get a new 'nums' as well as returning nums.length