class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        cur = root
        res = []
        while cur != None:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            # left subtree exists
            else:
                pre = cur.left
                # get the rightmost node in the left subtree
                while pre.right and pre.right != cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res
