# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max = float("-inf")

        def dfs(node):
            if not node:
                return 0
            left_maxgain = max(dfs(node.left), 0)
            right_maxgain = max(dfs(node.right), 0)
            maximum = node.val + left_maxgain + right_maxgain
            self.max = max(self.max, maximum)
            # MIST: can't return both children here, only either path
            return node.val + max(left_maxgain, right_maxgain)
        dfs(root)
        return self.max
