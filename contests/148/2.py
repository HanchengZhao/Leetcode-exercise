# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # if x is root, unless one subtree has odd number of nodes,
        # the other sub is only one
        if n == 1 and x == 1:
            return False

        def findNode(node, val):
            if not node:
                return None
            if node.val == val:
                return node
            return findNode(node.left, val) or findNode(node.right, val)

        def getCount(node):
            if not node:
                return 0
            left = getCount(node.left)
            right = getCount(node.right)
            return left + right + 1
        firstNode = findNode(root, x)
        leftCount = getCount(firstNode.left)
        rightCount = getCount(firstNode.right)
        rest = n - leftCount - rightCount - 1
        if rest > (leftCount + rightCount) or leftCount > (rest + rightCount) \
                or rightCount > (leftCount + rest):
            return True
        return False
