/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if(p==null || q==null) {
        return p==q;
    } else 
        return (p.val == q.val)&&isSameTree(p.left,q.left)&&isSameTree(p.right,q.right);
};

// var inOrderTraversal = function(node, arr){ 
//     if (node !== null){
//     inOrderTraversal(node.left, arr);
//     arr.push(node.val);
//     inOrderTraversal(node.right, arr);
        
//     }
    
// }