/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var rowSet = new Set();
    var colSet = new Set();
    var blockSet = new Set();
    for(var row = 0; row < 9; row++){
        for(var col = 0; col < 9; col++){
            var data = board[row][col];
            var block_num = Math.floor(col / 3) * 3 + Math.floor(row / 3);
            if(data !== "."){
                if(rowSet.has(row+data)){
                    return false;
                }else{
                    rowSet.add(row+data);

                }
                if(colSet.has(col+data)){
                    return false;
                }else{
                    colSet.add(col+data);
                }
                if(blockSet.has(block_num+data)){
                    return false;
                }else{
                    blockSet.add(block_num+data);
                }
            }
        }
    }
    
    return true;
};

// var time1 = new Date().getTime();
// var board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"];
// console.log(isValidSudoku(board));
// var time2 = new Date().getTime();

// console.log(time2 - time1);