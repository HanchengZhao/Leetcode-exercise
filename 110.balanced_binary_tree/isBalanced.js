/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    if(root === null) return true;
    var dif = Math.abs(height(root.left)-height(root.right));
    if (dif > 1) return false;
    return isBalanced(root.left)&&isBalanced(root.right);
    
};

var height = function(node){
    if(node === null) return 0;
    return 1+ Math.max(height(node.left), height(node.right));
}