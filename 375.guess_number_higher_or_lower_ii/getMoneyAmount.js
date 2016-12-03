/**
 * @param {number} n
 * @return {number}
 */
var getMoneyAmount = function(n) {
    var table = new Array(n+1);
    for (let i = 0; i < n+1; i++) {
      table[i] = new Array(n+1);
    }
    return DP(table, 1, n);
};

var DP = function(table, start, end){
    if (start >= end) return 0;
    if(table[start][end] != undefined) return table[start][end];
    var res = Number.MAX_SAFE_INTEGER;
    for(var i = start; i < end; i++){
        var temp = i + Math.max(DP(table, start, i-1), DP(table, i+1, end));
        res = Math.min(res, temp);
    }
    table[start][end] = res;
    return res;
};
console.log(getMoneyAmount(5));

//https://en.wikipedia.org/wiki/Minimax