# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        res = [0] * len(nodes)
        stack = []
        for i, val in enumerate(nodes):
            if not stack:
                stack.append((val, i))
            else:
                while stack and val > stack[-1][0]:
                    last = stack.pop()
                    res[last[1]] = val
                stack.append((val, i))
        return res
