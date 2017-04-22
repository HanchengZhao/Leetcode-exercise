# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            size = len(queue)
            temp = float('-inf')
            while size:
                node = queue.pop(0)
                temp = max(temp, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            res.append(temp)

        return res