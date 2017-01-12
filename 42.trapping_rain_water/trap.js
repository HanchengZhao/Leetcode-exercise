/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    if (height.length === 0 || height.length === 1){
        return 0;
    }
    var pre = 0;
    var latter = height.length-1;
    var result = 0;
    // pre++;
    // latter--;
    while(pre < latter){
        if(height[pre] <= height[latter]){
            pre++;
            if(height[pre] < height[pre-1]){
                result += height[pre-1] - height[pre];
                height[pre] = height[pre-1];
            }
        }else{
            latter--;
            if(height[latter] < height[latter+1]){
                result += height[latter+1] - height[latter];
                height[latter] = height[latter+1];
            }
        }
    }
    return result;
};

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));