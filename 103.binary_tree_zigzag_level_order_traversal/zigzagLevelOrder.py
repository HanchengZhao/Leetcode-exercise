# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [] #save the nodes for bfs
        stack = [] #save the node values
        result = []
        queue.append(root)
        stack.append(root.val)
        sign = 1 #indicate direction
        while len(queue):
            result.append(stack)
            stack = [] #empty the stack for next use
            size = len(queue)
            while size:
                node = queue.pop(0)
                if(node.left):
                    queue.append(node.left)
                    if sign == 1:
                        stack.insert(0, node.left.val)
                    else:
                        stack.append(node.left.val)
                if(node.right):
                    queue.append(node.right)
                    if sign == 1:
                        stack.insert(0, node.right.val)
                    else:
                        stack.append(node.right.val)
                print stack
                size -= 1
            sign *= -1
        return result
