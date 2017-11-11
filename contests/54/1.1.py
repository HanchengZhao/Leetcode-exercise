class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        degree = 0
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            degree = max(degree, dic[i])
        candidates = set()
        for k in dic.keys():
            if dic[k] == degree:
                candidates.add(k)
        firstleft = {}
        smallest = len(nums)
        for i in xrange(len(nums)):
            if nums[i] in candidates and nums[i] not in firstleft:
                firstleft[nums[i]] = i
        for j in xrange(len(nums)-1,-1,-1):
            if nums[j] in candidates:
                length = j - firstleft[nums[j]]+1
                smallest = min(smallest, length)
                candidates.remove(nums[j])
        return smallest
        
s = Solution()
print s.findShortestSubArray([2,1])