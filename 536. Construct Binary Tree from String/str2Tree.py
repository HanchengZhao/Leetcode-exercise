# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        stack = []
        i = 0
        while i < len(s):
            j = i # mark the starting point
            c = s[i]
            if c == ')': # node is used
                stack.pop() 
            elif c.isdigit() or c == '-' :
                while i + 1 < len(s) and s[i+1].isdigit(): # gather the number, e.g. '-12' or '123'
                    i += 1
                curNode = TreeNode(int(s[j:i+1]))
                if len(stack) != 0:
                    parent = stack[-1]
                    # check if left node is already occupied, otherwise add to right
                    if parent.left: 
                        parent.right = curNode
                    else:
                        parent.left = curNode
                stack.append(curNode)
            i += 1
        return stack[-1] # in the end, there is only root node left