# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prefix = {0: dummy}
        node = head
        s = 0
        while node:
            s += node.val
            if s in prefix:
                prev = prefix[s]
                prev.next = node.next
                node = dummy.next
                s = 0
                prefix = {0: dummy}
            else:
                prefix[s] = node
                node = node.next
        return dummy.next
