class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if k == 1:
            return True
        if n < k:
            return False
        s = sum(nums)
        if s % k != 0:
            return False
        sub = s / k
        subsetSum = [0] * n
        taken = [False] * n
        return self.helper(nums, subsetSum, taken, sub, k, n, 0, n-1)
    def helper(self, nums, subsetSum, taken, sub, k, n, cur, limit):
        if subsetSum[cur] == sub:
            if cur == k-2:
                return True
            return self.helper(nums, subsetSum, taken, sub, k, n, cur+1, n-1)
        for i in xrange(limit, -1, -1):
            if taken[i]:
                continue
            temp = subsetSum[cur] + nums[i]
            if temp <= sub:
                taken[i] = True
                subsetSum[cur] += nums[i]
                nxt = self.helper(nums, subsetSum, taken, sub, k, n, cur, i-1)
                taken[i] = False
                subsetSum[cur] -= nums[i]
                if nxt:
                    return True
        return False
s = Solution()
print s.canPartitionKSubsets([2, 1, 4, 5, 3, 3], 3)