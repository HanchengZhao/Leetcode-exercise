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
        return self.traverse(s,t)
    def traverse(self, s, t):
        return s != None and (self.equal(s,t) or self.traverse(s.left, t) or self.traverse(s.right, t))
    def equal(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.equal(s.left, t.left) and self.equal(s.right, t.right)