# https://www.youtube.com/watch?v=Dte6EF1nHNo 
'''
            1
          /  \
         2    3
        / \  / \
       4   5 6  7
->  <-4<->5<->2<->1<->3<->6<->7->

'''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution(object):
    def concatenate(self, a, b):
        if not a:
            return b
        if not b:
            return a
        # since it is a circular list
        aEnd = a.left
        bEnd = b.left
        # concatenate head and tail
        a.left = bEnd
        aEnd.right = b
        b.left = aEnd
        bEnd.right = a
        return a 

    def treeToList(self, n):
        if not n:
            return n
        leftList = self.treeToList(n.left)
        rightList= self.treeToList(n.right)
        # make single node is self linked
        n.left = n
        n.right = n
        # concatenate left subtree and right subtree
        n = self.concatenate(leftList, n)
        n = self.concatenate(n, rightList)
        return n
'''
it is basically a modified in-order traverse of binary tree, every time 
concatenate left subtree and parent node, parent node and right subtree.
In order to make circur link work, link the node to itself first.
'''