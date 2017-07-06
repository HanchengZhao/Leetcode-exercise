class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = { 0 : 1 }
        prefixSum = 0
        res = 0
        for num in nums:
            prefixSum += num
            delta = prefixSum - k #help define the starting point
            res += dic.get(delta, 0)
            dic[prefixSum] = dic.get(prefixSum, 0) + 1

        return res
#TLE
s = Solution()
print s.subarraySum([0,0,0,0,0,0,0,0,0,0]
,0)