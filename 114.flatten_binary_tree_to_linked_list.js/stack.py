class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        stack = []
        if root:
            p = root
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            p.right = node
            p.left = None
            p = p.right
            