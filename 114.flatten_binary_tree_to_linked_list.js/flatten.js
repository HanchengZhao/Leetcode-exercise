/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */


var flatten = function(root) {
    if(root !== null){
    
    var pre = null;
    flatten(root.right);
    flatten(root.left);
    
    root.right = pre;
    root.left = null;
    pre = root;
    }
};