/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    if(root === null) return [];
    var node_queue = [];
    var value_queue = [];//record the remaining sum value
    var path_queue =[];//store the path
    var answer = [];
    var path = [];
    path.push(root.val);
    node_queue.push(root);
    value_queue.push(sum - root.val);
    path_queue.push(path);
    
    while(node_queue.length > 0){
        var node  = node_queue.shift();
        var value = value_queue.shift();
        path = path_queue.shift();
        if(node.left === null && node.right === null && value === 0){
            answer.push(path);
        }
        if(node.left !== null ){
            node_queue.push(node.left);
            value_queue.push(value - node.left.val);
            var path_left = path.slice();//deep copy
            path_left.push(node.left.val);
            path_queue.push(path_left);
        }
        if(node.right !== null ){
            node_queue.push(node.right);
            value_queue.push(value - node.right.val);
            var path_right = path.slice();
            path_right.push(node.right.val);
            path_queue.push(path_right);
        }
    }
    return answer;
};