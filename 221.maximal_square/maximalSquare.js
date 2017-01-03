/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    var n = matrix.length;
    if(n === 0){
        return 0;
    }

    var m = matrix[0].length;
    if(m === 0){
        return 0;
    }
    // console.log("pass");
    var s = new Array(n+1);
    for(var i = 0; i < n+1; i++){
        s[i] = new Array(m+1);
        s[i].fill(0);
    }//initilize the 2d array
    // s[0][0] = matrix[0][0];
    var ans = 0;

    for(let i = 1; i <= n; i++){
        for(let j = 1; j <= m; j++){
            if(matrix[i-1][j-1] === "0"){
                s[i][j] = 0;
            }else{
                s[i][j] = Math.min(s[i-1][j-1], Math.min(s[i][j-1], s[i-1][j])) + 1;
                // console.log(s[i][j]);
            }
            if (s[i][j] > ans) ans = s[i][j];
        }
    }
    return ans * ans;
};

console.log(maximalSquare(["10100","10111","11111","10010"]));