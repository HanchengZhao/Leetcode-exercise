# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        res = False
        if not s and not t:
            return True
        if s and t :
            if s.val == t.val:
                res = self.isSameTree(s,t) or res
            res = self.isSubtree(s.left, t) or res
            res = self.isSubtree(s.right, t) or res
        return res

    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if a and b:
            if a.val == b.val:
                return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
        else:
            return False
