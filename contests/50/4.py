
from itertools import permutations
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def valid(comb, sum):
            if not comb:
                return int(abs(sum)) == 24
            mul = 1 if len(comb) == 4 else sum
            div = comb[0] ** 2 if len(comb) == 4 else sum
            return any([valid(comb[1:], sum + comb[0]), valid(comb[1:], sum - comb[0]), valid(comb[1:], mul * comb[0]), valid(comb[1:], float(div) / comb[0])])
        perm = permutations(nums)
        for p in perm:
            print p
            if valid(p, 0):
                return True
        return False
s = Solution()
print s.judgePoint24([1, 3, 4, 6])