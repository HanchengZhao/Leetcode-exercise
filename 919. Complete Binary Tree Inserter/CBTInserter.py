# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class CBTInserter:
    # BFS the tree and push any node that's not fulfilled by 2 children to the deque
    def __init__(self, root: TreeNode):
        self.root = root
        self.deque = deque()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    # append the new node to the end of deque
    # then set it as a childnode of the first node in the deque
    def insert(self, v: int) -> int:
        self.deque.append(TreeNode(v))
        node = self.deque[0]
        if not node.left:
            node.left = self.deque[-1]
        elif not node.right:
            node.right = self.deque[-1]
            # it's fullfilled by 2 nodes, so pop out
            self.deque.popleft()
        return node.val

    def get_root(self) -> TreeNode:
        return self.root
        