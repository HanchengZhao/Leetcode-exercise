class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == p or root == q or not root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left != None and  right != None:
            return root
        else:
            return left if left else right
'''
If the current (sub)tree contains both p and q, then the function result is their LCA. 
If only one of them is in that subtree, then the result is that one of them. 
If neither are in that subtree, the result is null/None/nil.
'''
