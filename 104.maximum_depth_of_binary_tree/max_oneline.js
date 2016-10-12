var maxDepth = function(root) {
    return root === null ? 0: Math.max(maxDepth(root.left),maxDepth(root.right))+1;
};