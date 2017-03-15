class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        comb = []
        candidates.sort()
        index = 0
        self.helper(candidates, target, res, comb, index)
        return res

    def helper(self, candidates, target, res, comb, index):
        if target < 0:
            return
        if target == 0:
            res.append(comb)
        for i in xrange(index,len(candidates)): #avoid duplicates
                self.helper(candidates, target - candidates[i], res, comb+[candidates[i]], i)
s = Solution()
print s.combinationSum([2,3,6,7], 7)