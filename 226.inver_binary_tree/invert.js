/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (root === null) return null;
    if (root.left === null && root.right === null) return root;
    var tempRight = root.right;
    root.right = invertTree(root.left);
    root.left = invertTree(tempRight);
    return root;
    
};