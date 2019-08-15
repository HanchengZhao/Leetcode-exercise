# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def findNode(root, val):
            if not root:
                return None
            if root.val == val:
                return root
            return findNode(root.left, val) or findNode(root.right, val)
        roots = []
        roots.append(root)
        for d in to_delete:
            while roots:
                i = roots.pop(0)
                node = findNode(i, d)
                if node is not None:
                    if i.val != node.val:
                        roots.append(i)
                    if node.left:
                        roots.append(node.left)
                    if node.right:
                        roots.append(node.right)
                    # node here is just a variable pointing to the tree node
                    # changing its assignment doesn't necessarily change the tree structure
                    # we need to change its parent's subtree assginment
                    node = None
                    break
                else:
                    roots.append(i)
        return roots
