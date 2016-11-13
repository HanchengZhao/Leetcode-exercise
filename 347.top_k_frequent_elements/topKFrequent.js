/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var frequenceMap = new Map();
    for(var elem in nums){//set up the frequence map
        var val = frequenceMap.get(nums[elem]);
        if(val === undefined){
            frequenceMap.set(nums[elem],1);
        }else{
            frequenceMap.set(nums[elem],val+1);
        }
    }
    
    var bucket = new Array(nums.length+1);
    frequenceMap.forEach(function(freq,num){
        if(bucket[freq] === undefined){
            bucket[freq] = [];
        }
        bucket[freq].push(num);
    });
    
    var result = [];
    for(var i = bucket.length-1; i>0 && k>0; i--){
        if(bucket[i] !== undefined){
            result = result.concat(bucket[i]);
            k -= bucket[i].length;
        }
    }
    
    return result;
    
    
};

console.log(topKFrequent([1,1,1,2,2,3],2));

//notes:
// for(var elem in nums)  // elem is the index

//array concatenate: result = result.concat(bucket[i]);