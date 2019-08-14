class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        every element can be or not be in a subset, so there are totally
        2^n combinations. We can start from the 1st element and add lists that with
        it or without it, and iterate each elements.
        if the nums = [1,2,3] the process could be [[]] -> [[],[1]] -> [[],[1],[2],[1,2]]
        -> [[],[1],[2],[1,2], [3],[1,3],[2,3],[1,2,3]]
        """

        if not nums:
            return [[]]
        res = [[]]
        index = 0
        while index < len(nums):
            res +=  [i + [nums[index]] for i in res]
            index += 1
        return res
s = Solution()
print s.subsets([1,2,3])

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            res += [[i] + j for j in res]
        return res