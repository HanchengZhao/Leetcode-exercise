# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# the basic idea is to traverse the tree in order, the first node that value is bigger than the previous one
# and the node with the value smaller than the previous one would be the nodes that we want


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.secondNode = None
        self.prevNode = TreeNode(float("-inf"))

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.firstNode and self.prevNode.val > root.val:
                self.firstNode = self.prevNode
            # if the firstNode is found
            if self.firstNode and self.prevNode.val > root.val:
                self.secondNode = root
            self.prevNode = root
            dfs(root.right)
        dfs(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val
