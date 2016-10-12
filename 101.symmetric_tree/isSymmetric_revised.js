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
var isSymmetric = function(root) {
    if (root === null) return true;
    return isMirror(root.left,root.right);
};

var isMirror = function(left,right){
    if(left===null&&right===null) return true;
    if(left===null||right===null) return false;
    return (left.val===right.val)&&isMirror(left.left,right.right)&&isMirror(left.right,right.left);
}