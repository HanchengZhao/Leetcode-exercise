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
var levelOrderBottom = function(root) {
    var result = [];
    if(root === null) return result;

    var curLevelCount = 1;
    var nextLevelCount = 0;
    var temp =[];//value array
    var queue = [];//node array
    queue.push(root);
    while(queue.length !== 0){
        curLevelCount--;
        var node = queue.shift();
        temp.push(node.val);
        if(node.left !== null){
            queue.push(node.left);
            nextLevelCount++;
        }
        if(node.right !== null){
            queue.push(node.right);
            nextLevelCount++;
        }
        if(curLevelCount === 0){
            result.unshift(temp);
            curLevelCount = nextLevelCount;
            nextLevelCount = 0;
            temp = [];
        }

    }
    return result;
};