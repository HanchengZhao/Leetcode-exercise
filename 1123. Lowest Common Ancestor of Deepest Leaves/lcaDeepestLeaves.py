# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import functools


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def recursion(root):
            if root is None:
                # depth, node
                return 0, None
            ld, left = recursion(root.left)
            rd, right = recursion(root.right)
            # return the deeper lca
            if ld > rd:
                return ld + 1, left
            elif rd > ld:
                return rd + 1, right
            else:
                return ld + 1, root
        return recursion(root)[1]
