#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recursion(cur, cursum, candidates, target, res, index):
            if cursum > target:
                return
            if cursum == target:
                res.append(cur)
                return 
            # we can only use the numbers at/after this index to avoid duplicates
            for i in range(index, len(candidates)):
                num = candidates[i]
                recursion(cur + [num], cursum + num, candidates, target, res, i)
        res = []
        recursion([], 0, candidates, target, res, 0)
        return res

