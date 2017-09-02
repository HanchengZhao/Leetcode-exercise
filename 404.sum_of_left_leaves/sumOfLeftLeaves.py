# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.dfs(root)
        return self.sum
    
    def dfs(self, root):
        if not root:
            return
        if root.left:
            if not root.left.left and not root.left.right: # left leaves
                self.sum += root.left.val
            else:
                self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
'''
left leaves, not left nodes
'''