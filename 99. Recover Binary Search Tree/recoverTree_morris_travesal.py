# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use morris traversal to reach space O(1) traversal, find out the misreplaced nodes in the process


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        # only update prevNode when moving to the right
        prevNode = TreeNode(float("-inf"))
        cur = root
        while cur is not None:
            if cur.left is None:
                # update first node and second node together
                if prevNode.val > cur.val:
                    if firstNode is None:
                        firstNode = prevNode
                        secondNode = cur
                    else:
                        secondNode = cur
                prevNode = cur
                cur = cur.right
            else:
                pre = cur.left
                # find the rightmost node
                while pre.right and pre.right != cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    if prevNode.val > cur.val:
                        if firstNode is None:
                            firstNode = prevNode
                            secondNode = cur
                        else:
                            secondNode = cur
                    # remove the link
                    pre.right = None
                    prevNode = cur
                    cur = cur.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
