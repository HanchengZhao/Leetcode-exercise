# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.maximum = 0

        def recursion(root):
            if not root:
                return 0, 0
            left_sum, left_count = recursion(root.left)
            right_sum, right_count = recursion(root.right)
            s = left_sum + right_sum + root.val
            count = left_count + right_count + 1
            avg = s / count
            self.maximum = max(self.maximum, avg)
            return s, count
        recursion(root)
        return self.maximum

# for tree questions, we can usually use a bottom-up solution to return the
# information to the every level above to solve recursively
# time: O(n)
