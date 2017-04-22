# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = [float("inf"), root.val]
        while root != None:
            if closest[0] > abs(target - root.val):
                closest[0] = abs(target - root.val)
                closest[1] = root.val
            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            elif root.val == target:
                return root.val
        return closest[1]