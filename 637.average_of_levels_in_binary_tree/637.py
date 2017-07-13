# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        queue = []
        avg = []
        queue.append(root)
        while queue:
            level_num = len(queue)
            node_num = len(queue)
            node_sum = 0
            while level_num:
                node = queue.pop(0)
                node_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_num -= 1
            avg.append(float(node_sum) / node_num)
        return avg
# [10,5,15,null,null,6,20]
# using bfs, get the value on each level and divide by node number