from collections import deque
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        queue = deque()
        maxLen = 0
        cost = maxCost
        for i in range(len(s)):
          diff = abs(ord(s[i]) - ord(t[i]))
          while queue and diff > cost:
              left = queue.popleft()
              cost += left
          if diff <= cost:
            queue.append(diff)
            cost -= diff
            maxLen = max(maxLen, len(queue))
          else:
            cost = maxCost
        return maxLen

s = Solution()

print(s.equalSubstring("abcd", "bcdf", 3))
print(s.equalSubstring("abcd", "cdef", 3))
print(s.equalSubstring("abcd", "acde", 0))
            