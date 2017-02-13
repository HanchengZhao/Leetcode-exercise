/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */

// function TreeNode(val) {
//     this.val = val;
//     this.left = this.right = null;
// }
var buildTree = function(inorder, postorder) {
    return helper(postorder.length-1, 0, inorder.length-1, inorder, postorder);
};

var helper = function(postIndex, inStart, inEnd, inorder, postorder){
    if (postIndex < 0 || inStart > inEnd) {
        return null;
    }
    var root = new TreeNode(postorder[postIndex]);
    var inIndex = inorder.indexOf(root.val);

    root.right = helper(postIndex-1, inIndex+1, inEnd, inorder, postorder);
    root.left = helper(postIndex-(inEnd-inIndex+1), inStart, inIndex-1, inorder, postorder);

    return root;
};

console.log(buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1]));