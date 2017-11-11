class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findsub(n, nums):
            i, j = 0, len(nums)-1
            while nums[i] != n:
                i += 1
            while nums[j] != n:
                j -= 1
            return j-i+1
        dic = {}
        degree = 0
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            degree = max(degree, dic[i])
        candidates = []
        for k in dic.keys():
            if dic[k] == degree:
                candidates.append(k)
        smallest = len(nums)
        for c in candidates:
            sm = findsub(c, nums)
            smallest = min(smallest, sm)
        return smallest
        
s = Solution()
print s.findShortestSubArray([2,1])