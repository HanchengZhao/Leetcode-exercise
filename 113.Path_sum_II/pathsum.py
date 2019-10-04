# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        
        def dfs(root, curPath, curSum):
            if not root.left and not root.right:
                if curSum + root.val == sum:
                    curPath.append(root.val)
                    self.res.append(curPath)
                    return
            if root.left:
                dfs(root.left, curPath + [root.val], curSum + root.val)
            if root.right:
                dfs(root.right, curPath + [root.val], curSum + root.val)
        dfs(root, [], 0)
        return self.res