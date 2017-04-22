# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = []
        count = 0
        queue.append(root)
        while len(queue) != 0:
            #nodes in each level
            size = len(queue)
            while(size):
                node = queue.pop(0)
                if (node.left == None and node.right == None):
                    return count+1
                if (node.left != None):
                    queue.append(node.left)
                if (node.right != None):
                    queue.append(node.right)
                size -= 1
            count += 1

        return count