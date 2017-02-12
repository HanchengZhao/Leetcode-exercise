# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The basic idea is here:
# Say we have 2 arrays, PRE and IN.
# Preorder traversing implies that PRE[0] is the root node.
# Then we can find this PRE[0] in IN, say it's IN[5].
# Now we know that IN[5] is root, so we know that IN[0] - IN[4] is on the left side, IN[6] to the end is on the right side.
# Recursively doing this on subarrays, we can build a tree out of it :)


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, 0, len(inorder)-1, preorder, inorder)

    def helper(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart > len(preorder)-1 or inStart > inEnd:
            return None
        rootVal = preorder[preStart]
        root = TreeNode(rootVal)

        inIndex = inorder.index(rootVal)
        root.left = self.helper(preStart+1, inStart, inIndex-1, preorder,inorder)
        root.right = self.helper(preStart+inIndex-inStart+1, inIndex+1, inEnd, preorder, inorder)
        return root