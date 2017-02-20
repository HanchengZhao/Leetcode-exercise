# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = []
        longest = 0
        queue.append([root,1])
        while queue:
            size = len(queue)
            while size:
                node = queue.pop(0)
                longest = max(node[1],longest)
                if node[0].left:
                    if node[0].left.val - node[0].val == 1:
                        queue.append([node[0].left,node[1]+1])
                    else:
                        queue.append([node[0].left,1])
                if node[0].right:
                    if node[0].right.val - node[0].val == 1:
                        queue.append([node[0].right,node[1]+1])
                    else:
                        queue.append([node[0].right,1])
                size -= 1
        return longest