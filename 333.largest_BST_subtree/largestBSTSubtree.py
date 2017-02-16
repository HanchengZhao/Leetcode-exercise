# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Subtree(object):
    def __init__(self, largest, n, Min, Max):
        self.largest = largest
        self.n = n
        self.Min = Min
        self.Max = Max


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.dfs(root)
        return res.largest

    def dfs(self, root):
        if not root:
            return Subtree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val > left.Max and root.val < right.Min:
            n = left.n + right.n + 1
        else:
            n = float('-inf')
            # TODO: write code...
        largest = max(left.largest, right.largest, n)
        return Subtree(largest, n, min(root.val, left.Min), max(root.val, right.Max))