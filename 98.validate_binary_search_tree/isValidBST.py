# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        self.inOrder(root, output)
        for i in range(1, len(output)):
            if output[i] <= output[i-1]:
                return False
        return True

    def inOrder(self, parent, output):
        if not parent:
            return
        self.inOrder(parent.left, output)
        output.append(parent.val)
        self.inOrder(parent.right, output)
