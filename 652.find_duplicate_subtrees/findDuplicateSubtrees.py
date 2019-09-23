class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = {}
        res = []

        def dfs(root):
            if not root:
                return "#"
            serial = "{}.{}.{}".format(
                root.val, dfs(root.left), dfs(root.right))
            count[serial] = count.get(serial, 0) + 1
            if count[serial] == 2:
                res.append(root)
            return serial
        dfs(root)
        return res


'''
use dfs to serialize each subtree and check duplicates
'''
