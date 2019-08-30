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
        if not root:
            return True
        stack = []
        pre = TreeNode(None)
        while root or stack != []:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True
