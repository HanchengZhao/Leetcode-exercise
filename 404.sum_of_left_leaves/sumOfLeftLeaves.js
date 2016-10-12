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
var sumOfLeftLeaves = function(root) {
    return sumofleftleaves(root);
};

//traverse the tree with a flag noting from left or right
var sumofleftleaves =function(root, isLeft){
    if(root === null) return 0;
    var sum = 0;
    if(root.left === null && root.right === null && isLeft){
        sum += root.val;
    }
    
    sumofleftleaves(root.left, true);
    sumofleftleaves(root.right, false);
    return sum;
    
}