# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        def getlen(root):
            if not root:
                return 0
            l = 1
            node = root
            while node.next:
                l += 1
                node = node.next
            return l

        length = getlen(root)
        res = [None] * k
        if length < k:
            node = root
            i = 0
            while node:
                dummy = node
                res[i] = dummy
                node = node.next
                dummy.next = None
                i += 1
        else:
            dummy = ListNode(0)
            dummy.next = root
            div = length / k
            mod = length % k
            for i in xrange(k):
                prev = dummy
                res[i] = dummy.next
                for j in xrange(div+(1 if mod > 0 else 0)):
                    dummy = dummy.next
                prev.next = None
                mod -= 1
        return res