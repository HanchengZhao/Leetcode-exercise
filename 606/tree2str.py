# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        self.res = ""
        self.preoder(t)
        return self.res

    def preoder(self, t):
        if t:
            self.res += str(t.val)
        if not t.left and not t.right:
            return
        if t.left:
            self.res += '('
            self.preoder(t.left)
            self.res += ')'
        if not t.left:
            self.res += "()"
        if t.right:
            self.res += '('
            self.preoder(t.right)
            self.res += ')'
