/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
  let res = [];
  dfs(root, res);
  return res;
};

function dfs(root, res) {
  if (!root) return;
  res.push(root.val);
  dfs(root.left, res);
  dfs(root.right, res);
}
