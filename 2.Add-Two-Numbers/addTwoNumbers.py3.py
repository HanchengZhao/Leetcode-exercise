# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        carry = 0
        while l1 != None or l2 != None:
            if l1 and l2:
                newValue = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            # only one linkedlist has valid node
            elif l1:
                newValue = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                l1 = l1.next
            else:
                newValue = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                l2 = l2.next
            head.next = ListNode(newValue)
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return dummy.next

# things to notice:
# - use carry for digit overflow
# - use a dummy node to track the head node
# - always remember to proceed the list node to the next one
# time complexity: O(m + n), m for length of l1, n for l2
# space complexity: O(m + n)
