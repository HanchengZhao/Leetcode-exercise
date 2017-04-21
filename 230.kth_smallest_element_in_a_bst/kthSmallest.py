# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = collections.deque(maxlen=k)
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right