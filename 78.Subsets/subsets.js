var subsets = function(nums){
    var results = [];
    if(nums === null || nums.length === 0){
        return results;
    }
    nums.sort(function(a,b){return a-b});
    var subset = [];
    subsetsHelper(nums, 0, subset, results);
    
    return results;
};

var subsetsHelper = function(nums, startIndex, subset, results){
    results.push(subset.slice());//deep copy
    for(var i = startIndex; i < nums.length; i++){
        subset.push(nums[i]);
        subsetsHelper(nums, i+1, subset, results);
        subset.pop();
    }
};


console.log(subsets([1,2,3,4,5,6,7]));
