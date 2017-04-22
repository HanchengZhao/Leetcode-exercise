/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    var num = [];
    for (var i of nums) {
        num.push(i.toString());
    }
    num.sort(function(a,b){
        if (a+b >= b+a){
            return -1;
        }else{
            return 1;
        }
    });
    var res = num.join("");
    //remove the 0s on the left
    for(var j of res){
        if (j != "0") break;
        res = res.substring(1);
    }
    return res || "0";
};

console.log(largestNumber([0,0]));