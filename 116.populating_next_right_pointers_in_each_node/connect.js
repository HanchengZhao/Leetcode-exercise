/**
 * Definition for binary tree with next pointer.
 * function TreeLinkNode(val) {
 *     this.val = val;
 *     this.left = this.right = this.next = null;
 * }
 */

/**
 * @param {TreeLinkNode} root
 * @return {void} Do not return anything, modify tree in-place instead.
 */
var connect = function(root) {
    // connect all the children
    if(root === null) return;

    if (root.left) {
        root.left.next = root.right;
    }
    // connect nodes between subtrees
    if (root.next && root.next.right){
        root.right.next = root.next.left;
    }

    connect(root.left);
    connect(root.right);

};