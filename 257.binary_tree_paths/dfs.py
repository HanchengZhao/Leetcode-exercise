class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: # null check
            return [] 
        res = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop() 
            if not node.left and not node.right:
                res.append(path+str(node.val))
            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))
            if node.right:
                stack.append((node.right, path + str(node.val) + '->'))
        return res
'''
use stack to store node and path in pair, every time the last tuple is popped, it goes into 
next level
'''