var hasPathSum = function(root, sum) {
    if(root === null) return false;
    if((sum - root.val) === 0 && root.left === null && root.right === null) return true;
    return hasPathSum(root.left,sum-root.val) || hasPathSum(root.right,sum-root.val);
};