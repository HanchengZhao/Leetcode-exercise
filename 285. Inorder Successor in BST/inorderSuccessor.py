# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else: # root is either the parent of p or a node from p's right subtree
            left = self.inorderSuccessor(root.left, p) # check if p has right subtree
            return left if left != None else root # return the node in p'right subtree, otherwise return the parent