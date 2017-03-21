# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        while root:
            head = TreeLinkNode(0)
            cur = head
            #traverse a level
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            #head.next will always point to the leftmost node in next level
            root = head.next




        # if not root:
        #     return None
        # while root:
        #     if root.next == None:
        #         leftmost = None
        #     if root.left and root.right:
        #         root.left.next = root.right
        #     head = root.right if root.right else root.left
        #     if not leftmost:
        #         leftmost = root.left if root.left else root.right
        #     neigh = root.next
        #     while neigh and head:
        #         if neigh.left:
        #             head.next = neigh.left
        #             break
        #         elif neigh.right:
        #             head.next = neigh.right
        #             break
        #         neigh = neigh.next
        #     root = root.next if root.next else leftmost