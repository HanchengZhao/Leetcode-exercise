# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node: #not null for node
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append("#")
        return " ".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "#":
            return None
        nodelist = data.split(" ")
        print nodelist
        root = TreeNode(nodelist.pop(0))
        queue = [root]
        while nodelist:
            parent = queue.pop(0)
            left = nodelist.pop(0)
            left = None if left == "#" else TreeNode(int(left))
            right = nodelist.pop(0)
            right = None if right == "#" else TreeNode(int(right))
            if left:
                parent.left = left
                queue.append(left)
            if right:
                parent.right = right
                queue.append(right)
        return root
'''
the basic idea is to use # to replace null in the string, when deserializing the string,
only add the not null value to the queue, which contains parents
'''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize("1 # # ")