# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)
        biggest = 1
        Sum = float("-inf")
        level = 0
        while queue:
            level += 1
            size = len(queue)
            levelSum = 0
            while size > 0:
                node = queue.pop(0)
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            if levelSum > Sum:
                biggest = level
                Sum = levelSum
        return biggest
