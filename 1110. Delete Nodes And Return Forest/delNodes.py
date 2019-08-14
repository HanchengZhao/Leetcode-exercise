# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# We first need to traverse the tree recursively to delete the node and get the new roots
# nodes will only be added to the result, if they:
# 1. not the nodes to be deleted
# 2. doesn't have parents
# this is a bottom up  recursion


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # make a set to get O(1) find
        to_delete = set(to_delete)
        roots = []

        def dfs(root, parent_exist):
            if root is None:
                return root
            if root.val in to_delete:
                dfs(root.left, False)
                dfs(root.right, False)
                return None
            else:
                if not parent_exist:
                    roots.append(root)
                root.left = dfs(root.left, True)
                root.right = dfs(root.right, True)
                return root
        dfs(root, False)
        return roots
