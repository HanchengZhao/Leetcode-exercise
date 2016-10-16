/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var single = [];
    nums.forEach(function(int){
        if(single.indexOf(int) === -1){
            single.push(int);
        }else{
            var index = single.indexOf(int);
            single.splice(index,1);
        }
    });
    return single.pop();
};