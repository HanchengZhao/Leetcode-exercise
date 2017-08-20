# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushAllLeft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.pushAllLeft(node.right)
        return node.val
        
    def pushAllLeft(self, node): # push all the left node to the stack
        while node:
            self.stack.append(node)
            node = node.left
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

'''
First push all the left nodes to the stack, and for each node popped, also push all the left node of its right one, it
is basically iterative in-order traversal of a tree
'''