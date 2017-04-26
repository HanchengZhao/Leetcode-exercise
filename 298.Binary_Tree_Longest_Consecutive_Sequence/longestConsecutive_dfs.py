# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.longest = 0
        self.dfs(root, 1)
        return self.longest

    def dfs(self, root, cur_len):
        self.longest = max(self.longest, cur_len)
        if root.left:
            if root.left.val - root.val == 1:
                self.dfs(root.left, cur_len+1)
            else:
                self.dfs(root.left, 1)
        if root.right:
            if root.right.val - root.val == 1:
                self.dfs(root.right, cur_len+1)
            else:
                self.dfs(root.right, 1)