# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        
        # 0 : all the nodes below are covered, but not this
        # 1 : all the nodes below and including this one are covered, no camera
        # 2 : all the nodes below and including this one are covered, but needs a camera here
        def dfs(root):
            if not root:
                return 0, 0, float("inf")
            L = dfs(root.left)
            R = dfs(root.right)
            
            dp0 = L[1] + R[1]
            # one of the child has camera
            dp1 = min(min(L[1], L[2]) + R[2], L[2] + min(R[1], R[2]))
            dp2 = 1 + min(L) + min(R)
            
            return dp0, dp1, dp2
        return min(dfs(root)[1:])