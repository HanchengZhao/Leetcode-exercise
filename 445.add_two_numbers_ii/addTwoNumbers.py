# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr1 = []
        arr2 = []
        while l1:
            arr1.append(str(l1.val))
            l1 = l1.next
        while l2:
            arr2.append(str(l2.val))
            l2 = l2.next
        sum = str(int("".join(arr1)) + int("".join(arr2)))
        dummy = ListNode(0)
        head = dummy
        while sum:
            head.next = ListNode(int(sum[0]))
            sum = sum[1:]
            head = head.next
        return dummy.next