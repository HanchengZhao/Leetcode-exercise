# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.height(root) # no need to get the return val, only focuses on the process
        return self.max
    # keep track of self.max in the process
    def height(self, root):
        if not root:
            return 0
        leftH = self.height(root.left)
        rightH = self.height(root.right)
        height = max(leftH, rightH) + 1 
        self.max = max(leftH + rightH, self.max) # not height
        return height
# longest path is the sum of left tree height and right tree height