var minDepth = function(root) {
    if(root === null) return 0;
    if(root.left === null || root.right === null){
        return minDepth(root.left)+minDepth(root.right)+1;
    }
    return Math.min(minDepth(root.left), minDepth(root.right))+1;
};
