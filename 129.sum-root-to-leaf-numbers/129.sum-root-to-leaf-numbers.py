#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.s = 0
        def dfs(prev, node):
            if not node.left and not node.right:
                self.s += prev * 10 + node.val
                return
            if node.left:
                dfs(prev * 10 + node.val, node.left)
            if node.right:
                dfs(prev * 10 + node.val, node.right)
        dfs(0, root)
        return self.s

            

