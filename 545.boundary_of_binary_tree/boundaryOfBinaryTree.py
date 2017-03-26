# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #left bound
        if not root:
            return []
        visited = set()
        leftp =[]
        leftp.append(root.val)
        visited.add(root)
        self.leftbound(root.left, visited, leftp)

        #leaves
        leaves = []
        self.dfs(root,visited,leaves)

        #rightbound
        rightp = []
        self.rightbound(root.right,visited,rightp)

        return leftp + leaves + rightp[::-1]


    def leftbound(self, root, visited, leftp):
        if not root:
            return
        visited.add(root)
        leftp.append(root.val)
        if root.left:
            self.leftbound(root.left, visited, leftp)
        elif root.right:
            self.leftbound(root.right, visited, leftp)
        else:
            return
    def dfs(self, root, visited, leaves):
        if not root.left and not root.right and root not in visited:
            leaves.append(root.val)
            visited.add(root)
        if root.left:
            self.dfs(root.left, visited, leaves)
        if root.right:
            self.dfs(root.right, visited, leaves)
    def rightbound(self, root, visited, rightp):
        if not root:
            return
        if root not in visited:
            rightp.append(root.val)
        if root.right:
            self.rightbound(root.right, visited, rightp)
        elif root.left:
            self.rightbound(root.left, visited, rightp)
        else:
            return