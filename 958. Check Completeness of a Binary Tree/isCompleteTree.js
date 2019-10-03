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
var isCompleteTree = function(root) {
  let queue = [root];
  let seenNull = false;
  while (queue.length > 0) {
    node = queue.shift();
    if (!node) {
      if (!seenNull) {
        seenNull = true;
      }
      continue;
    } else if (seenNull) {
      return false;
    }
    queue.push(node.left);
    queue.push(node.right);
  }
  return true;
};

/*
If it's a complete binary tree, we should not see other non-null nodes after
seeing the first null in the queue.
*/
