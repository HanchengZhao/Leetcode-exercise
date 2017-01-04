/**
 * @param {number[][]} matrix
 * @return {number}
 */
var dx = [1,-1,0,0];
var dy = [0,0,1,-1];//the step

var longestIncreasingPath = function(matrix) {
    "use strict";
    var search = function (x,y,matrix) {
        if(flag[x][y] !== 0){
            return dp[x][y]; //has been searched
        }
        var ans = 1;
        var nx,ny;
        for(var i = 0; i < 4; i++){
            nx = x + dx[i];
            ny = y + dy[i];
            if(0 <= nx && nx < n && 0 <= ny && ny < m){
                console.log(matrix[x][y],matrix[nx][ny]);
                if(matrix[x][y] > matrix[nx][ny]){

                    ans = Math.max(ans, search(nx, ny, matrix)+1);
                    console.log(ans);
                }
            }
        }
        flag[x][y] =1;
        dp[x][y]=ans;
        return ans;
    };

    var n = matrix.length;
    if(n == 0){
        return 0;
    }
    var m = matrix[0].length;
    // console.log(n,m);
    var dp = new Array(n);
    var flag = new Array(n);
    for(var i = 0; i < n; i++){
        dp[i] = new Array(m);
        dp[i].fill(0);
        flag[i] = new Array(n);
        flag[i].fill(0);
    }//initilize the 2d array
    var ans = 0;
    for(let i = 0; i < n; i++){
        for(let j = 0; j < m; j++){
            dp[i][j] = search(i,j,matrix);
            ans = Math.max(dp[i][j],ans);
            // console.log(dp[i][j]);
        }
    }
    return ans;

};


// console.log(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
console.log(longestIncreasingPath([[1,2,3,4]]));