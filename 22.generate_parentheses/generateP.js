/**
 * @param {number} n
 * @return {string[]}
 */
 // idea from https://discuss.leetcode.com/topic/8724/easy-to-understand-java-backtracking-solution
var generateParenthesis = function(n) {
    var list = new Array();
    backtrack(list, '', 0, 0, n);
    return list;
};

var backtrack = function(list, str, open, close, max){
    
    if(str.length == max * 2){
        list.push(str);
        return;
    }
    if(open < max)
        backtrack(list, str+"(", open+1, close, max);
    if(close < open)
        backtrack(list, str+")", open, close+1, max);
}//recursively call to get all the possible combinations;
//backtracking algorithm