# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root, lower=float("-inf"), upper=float("inf")):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            if not helper(root.left, lower, root.val):
                return False
            if not helper(root.right, root.val, upper):
                return False
            return True
        return helper(root)
