# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        p = head
        # get length
        l = 0
        while p:
            l += 1
            p = p.next
        if not l:
            return None
        k = k % l
        if not k or not head:
            return head
        fast = slow = head
        while k:
            fast = fast.next
            k -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
