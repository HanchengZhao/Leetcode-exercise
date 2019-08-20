import heapq
from collections import Counter


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counter = Counter(s)
        # use a heapq to track put most counted char
        h = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(h)
        # insert into new string separated by at least k
        newstring = []
        while len(newstring) < len(s):
            if not h:
                return ""
            freq1, char = heapq.heappop(h)
            newstring.append(char)
            # use a stack to keep track of all the used chars
            stack = []
            # we need to use other chars in next k-1 slots
            for i in range(k-1):
                # reach the end
                if len(newstring) == len(s):
                    return "".join(newstring)
                # if no extra pairs
                if not h:
                    return ""
                freq, nxt = heapq.heappop(h)
                newstring.append(nxt)
                if freq < -1:
                    stack.append((freq+1, nxt))
            while stack:
                heapq.heappush(h, stack.pop())
            if freq1 < -1:
                heapq.heappush(h, (freq1+1, char))
        return "".join(newstring)


s = Solution()
print(s.rearrangeString("aabbcc", 2))
print(s.rearrangeString("aaaacdeebbb", 2))
