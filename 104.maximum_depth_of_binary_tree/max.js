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
var maxDepth = function(root) {//bfs
    if(root === null) return 0;
    var queue = [];
    var count = 0;
    queue.push(root);
    while(queue.length !== 0){
        var size = queue.length;
        while(size-- > 0){
            var node = queue.shift();
            
            if(node.left){
                queue.push(node.left);
            }
            
            if(node.right){
                queue.push(node.right);
            }
        }
        count++;
    }
    return count;
};