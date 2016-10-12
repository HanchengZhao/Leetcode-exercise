var maxDepth = function(root) {//dfs
    if(root === null) return 0;
    
    var stack = [];
    var value = [];
    var max = 0;
    stack.push(root);
    value.push(1);
    while(stack.length !==0){
        var node = stack.pop();
        var temp = value.pop();
        max = Math.max(max, temp);
        if(node.left){
            stack.push(node.left);
            value.push(temp+1);
        }
        if(node.right){
            stack.push(node.right);
            value.push(temp+1);
        }
    }
    return max;
    
};