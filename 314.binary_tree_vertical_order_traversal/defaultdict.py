# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dic = defaultdict(list) # not ordereddict, since it records insert order, not sorted keys
        queue = []
        queue.append((root, 0))
        dic[0] = [root.val]
        while queue:
            levelnum = len(queue)
            while levelnum:
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, index-1))
                    dic[index-1].append(node.left.val)
                if node.right:
                    queue.append((node.right, index+1))
                    dic[index+1].append(node.right.val)
                levelnum -= 1
        res = []
        for key in sorted(dic.keys()):
            res.append(dic[key])
        return res
'''
use bfs to traverse the tree and record the vertical index of the nodes (O(n))
use a dictionary to record the nodes value under different indexes, which takes O(nlog(n))
total: O(nlog(n))
'''