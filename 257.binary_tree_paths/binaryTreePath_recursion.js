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
    var answer = [];
    if(root !== null) binaryTreeRecur(root,'',answer);
    return answer;
};

var binaryTreeRecur = function(root, path, answer){
    if (root.left === null && root.right === null) answer.push(path + root.val);
    if (root.left !== null) binaryTreeRecur(root.left, path + root.val + "->", answer);
    if (root.right !== null) binaryTreeRecur(root.right, path + root.val + "->", answer);
}