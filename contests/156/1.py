from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        c = Counter(arr)
        occ = Counter(c.values())
        for v in occ.values():
            if v > 1:
                return False
        return True
s = Solution()
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))