var hasPathSum = function(root, sum) {
    if(root === null) return false;
    var node_queue = [];
    var value_queue = [];//record the remaining sum value
    node_queue.push(root);
    value_queue.push(sum - root.val);
    while(node_queue.length > 0){
        var node  = node_queue.shift();
        var value = value_queue.shift();
        if(node.left === null && node.right === null && value === 0){
            return true;
        }
        if(node.left !== null ){
            node_queue.push(node.left);
            value_queue.push(value - node.left.val);
        }
        if(node.right !== null ){
            node_queue.push(node.right);
            value_queue.push(value - node.right.val);
        }
    }
    return false;
    
};
