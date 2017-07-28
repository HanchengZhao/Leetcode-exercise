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
var isValidBST = function(root) {
    if (root === null) {
        return true;
    }
    var arr = []
    inOrder(root, arr)
    for(var i = 0; i < arr.length-1; i++) {
        if (arr[i] >= arr[i+1]) {
            return false;
        }
    }
    return true;
};

var inOrder = function(root, arr) {
    if (root.left !== null) {
        inOrder(root.left, arr);
    }
    arr.push(root.val)
    if (root.right !== null) {
        inOrder(root.right, arr);
    }
}