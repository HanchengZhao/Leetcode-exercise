# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#In order to get O(1) space, the way to do it properly is to do two passes. One to find the highest number of occurrences of any value, and then a second pass to collect all values occurring that often.
class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.currVal = float("inf")
        self.currCount = 0
        self.maxCount = 0
        self.modeCount = 0
        self.modes = []
        self.inorder(root)
        self.modes = [0] * self.modeCount
        self.inorder(root)
        return self.modes


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.handleValue(root.val)
        self.inorder(root.right)

    def handleValue(self, val):
        if val != self.currVal:
            self.currVal = val
            self.currCount = 0
        self.currCount += 1
        if self.currCount > self.maxCount:
            self.maxCount = self.currCount
            self.modeCount = 1
        elif self.currCount == self.maxCount:
            if self.modes:
                self.modes[self.modeCount] = self.currVal
            self.modeCount += 1
