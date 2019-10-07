# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:  # has left
            return "{}({})".format(t.val, self.tree2str(t.left))
        return "{}({})({})".format(t.val, self.tree2str(t.left), self.tree2str(t.right))
