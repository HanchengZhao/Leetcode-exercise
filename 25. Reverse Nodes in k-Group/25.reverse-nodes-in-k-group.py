#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # set a dummynode to track the head node
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            count = 0
            # check if we still have k nodes in the list
            while r and count < k:
                r = r.next
                count += 1
            if count == k:  # we have enough nodes
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:  # not enough nodes
                return dummy.next

        # reverse k nodes, return the newhead, newtail
        # make prev.next = newhead, newtail.next = nextnode
