/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    var number = [];//result array
    if(root === null) return number;
    
    var temp = [];
    var curLevelCount = 1;
    var nextLevelCount = 0;
    var queue = [];
    queue.push(root);
    while(queue.length !== 0){
        var node = queue.shift();
        temp.push(node.val);
        curLevelCount--;
        
        if(node.left){
            queue.push(node.left);
            nextLevelCount++;
        }
        
        if(node.right){
            queue.push(node.right);
            nextLevelCount++;
        }
        
        if(curLevelCount === 0){
            number.push(temp);
            curLevelCount = nextLevelCount;
            nextLevelCount = 0;//!
            temp = [];
        }
        
    }
    return number;
 
};