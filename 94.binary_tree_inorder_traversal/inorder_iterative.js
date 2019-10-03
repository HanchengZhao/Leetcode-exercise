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
var inorderTraversal = function(root) {
  if (!root) {
    return [];
  }
  let stack = [];
  let res = [];
  let cur = root;
  // go to the leftmost node, push nodes to the stack along the way
  // go to the right subtree once the left subtree are all traversed
  while (cur || stack.length > 0) {
    while (cur) {
      stack.push(cur);
      cur = cur.left;
    }
    node = stack.pop();
    res.push(node.val);
    cur = node.right;
  }
  return res;
};
