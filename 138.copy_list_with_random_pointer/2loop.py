"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # 2 loops
        # first loop builds all the next nodes
        # and build a map from original to copied
        m = {}
        dummy = Node(-1, None, None)
        orig, cur = head, dummy
        while orig:
            cur.next = Node(orig.val, None, None)
            m[orig] = cur.next
            orig = orig.next
            cur = cur.next
        # second loop: set all the random pointers
        orig, cur = head, dummy.next
        while orig:
            if orig.random:
                cur.random = m[orig.random]
            orig = orig.next
            cur = cur.next
        return dummy.next
