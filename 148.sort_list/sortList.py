# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        h1, h2 = head, mid.next
        mid.next = None
        return self.merge(self.sortList(h1), self.sortList(h2))

    # find the middle pointer of the linkedlist
    def findMid(self, head):
        if not head or not head.next:
            return head
        fast = slow = head
        # make sure the middle node is the end of the first half
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    # merge 2 sorted linkedlist

    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h2.next, h1)
            return h2

# time: O(nlogn), space: O(1)
