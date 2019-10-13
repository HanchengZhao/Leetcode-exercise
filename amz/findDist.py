# DIstance between 2 nodes in BST
def findDist(bstDistance, node1, node2):
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def findLowestCommonAncestor(root, node1, node2):
        if node1 > node2:
            return findLowestCommonAncestor(root, node2, node1)
        while True:
            if root.val >= node1 and root.val <= node2:
                return root
            if root.val < node1:
                root = root.right
            else:
                root = root.left

    def calculateDist(root, node):
        ret = 0
        while root.val != node:
            if node > root.val:
                root = root.right
            else:
                root = root.left
            ret += 1
        return ret

    if node1 == node2 or not bstDistance:
        return 0
    root = TreeNode(bstDistance[0])
    for i in range(1, len(bstDistance)):
        node = root
        while True:
            if bstDistance[i] > node.val:
                if not node.right:
                    node.right = TreeNode(bstDistance[i])
                    break
                node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(bstDistance[i])
                    break
                node = node.left
    node = findLowestCommonAncestor(root, node1, node2)
    dist1 = calculateDist(node, node1)
    dist2 = calculateDist(node, node2)
    return dist1 + dist2


bstDistance = [2, 0, 3, 5, 6, 4, 7, 8, 1]
node1 = 1
node2 = 4
print(findDist(bstDistance, node1, node2))
