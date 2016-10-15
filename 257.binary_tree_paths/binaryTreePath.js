/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    var queue = [];//store each node
    var pathqueue = [];//store the node path
    var allPath = [];
    if(root === null) return allPath;
    var path = root.val.toString();
    queue.push(root);
    pathqueue.push(path);
    while(queue.length > 0){
        var node = queue.shift();
        path = pathqueue.shift();
        if(node.left === null && node.right === null){
            allPath.push(path);
        }
        if(node.left !== null){
            queue.push(node.left);
            var leftPath = path + "->" + node.left.val.toString();
            pathqueue.push(leftPath);
        }
        if(node.right !== null){
            queue.push(node.right);
            var rightPath = path + "->" + node.right.val.toString();
            pathqueue.push(rightPath);
        }
    }
    return allPath;
};