/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    var result = [];
    if(numRows === 0) return result;
    if(numRows === 1){
        result.push([1]);
        return result;
    }
    result.push([1]);
    if(numRows === 2){
        result.push([1,1]);
        return result;
    }
    result.push([1,1]);
    for(var i = 3; i <= numRows; i++){
        var lastRow = result[i-2].slice();//get the last array
        var newArr = [1,1];
        for(var j = 0; j < lastRow.length-1; j++){
            var val = lastRow[j]+lastRow[j+1];
            newArr.splice(j+1,0,val);//add each pair sum to the array
        }
        
        result.push(newArr);
    }
    return result;
};

console.log(generate(10));