/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if(root === null) return 0;
    var queue = [];
    var count = 0;
    queue.push(root);
    while(queue.length !== 0){
        var size = queue.length;//number of nodes in one level
        while(size-- > 0){
            var node = queue.shift(); 
            if (node.left === null && node.right === null){
                return count+1;
            }
            if(node.left !== null){
                queue.push(node.left);
            }
            if(node.right !== null){
                queue.push(node.right);
            }
        }
        count++;
    }
    return count;
};

//node.left !== null && node.right !== null