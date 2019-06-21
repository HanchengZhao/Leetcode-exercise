# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # record the answer in the process
        memo = {}

        def generateFrom(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            allTrees = []
            for i in range(start, end+1):
                # pick a node as root
                leftTrees = generateFrom(start, i-1)
                rightTrees = generateFrom(i+1, end)
                # construct the subtree
                for j in leftTrees:
                    for k in rightTrees:
                        newRoot = TreeNode(i)
                        newRoot.left = j
                        newRoot.right = k
                        allTrees.append(newRoot)
            memo[(start, end)] = allTrees
            return allTrees
        return generateFrom(1, n) if n else []
