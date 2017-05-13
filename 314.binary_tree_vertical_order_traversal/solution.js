/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var verticalOrder = function(root) {
    if(!root) return [];
    var hashmap = new Map();
    var queue = [];
    queue.push([root,0]);
    while ( queue.length !== 0 ) {
        var size = queue.length;
        while ( size ) {
            var candidate = queue.shift();

            // save in map
            var node = candidate[0];
            var index = candidate[1];
            if ( hashmap.has(index) ) {
                hashmap.get(index).push(node.val);// add new val
            } else {
                hashmap.set(index, [node.val]);
            }
            if ( node.left !== null ) {
                queue.push([node.left, index-1]);
            }
            if ( node.right !== null ) {
                queue.push([node.right, index+1]);
            }
            size--;
        }
    }
    var keys = [];
    for (var key of hashmap.keys()){
        keys.push(key);
    }
    keys.sort(function(a,b){
        return a-b;
    });
    var res = [];
    keys.forEach(function (key) {

        res.push(hashmap.get(key));
    });
    return res;
};