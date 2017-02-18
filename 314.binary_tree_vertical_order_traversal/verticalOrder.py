# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        index = 0
        queue = []
        queue.append([root,index])
        res = []
        dic = {}
        while queue:
            size = len(queue)
            while size:
                node = queue.pop(0)
                if dic.get(node[1]):
                    dic[node[1]].append(node[0].val)
                else:
                    dic[node[1]] = [node[0].val]
                if node[0].left:
                    queue.append([node[0].left, node[1]-1])
                if node[0].right:
                    queue.append([node[0].right, node[1]+1])
                size -= 1
        keys = sorted(dic.keys())
        for key in keys:
            res.append(dic[key])
        return res
