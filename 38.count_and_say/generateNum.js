var countAndSay = function(n) {
    var result = '';
    var count = 1;
    var nums = [];
    var length = 0;
    while((n % 10) !== 0){
        nums.push(n % 10);
        n = Math.floor(n / 10);
        length++;
    }
    nums.reverse();
    console.log(nums);
    for(var i = 0; i < length; i++){
    
    var pointer = nums[i];
    if(nums[i] === nums[i + 1]){
        count++;
    }else{
        result = result + count + pointer;
        count = 1;
    }
    }
    console.log(result);
    return result;
};