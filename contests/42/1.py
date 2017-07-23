class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup, missing = 0,0
        hashmap = {}
        res = []
        for i in xrange(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                res.append(nums[i])
        keys = sorted(hashmap.keys())
        for i in xrange(len(keys)):
            if keys[i] != i+1:
                res.append(i+1)
                break
            if len(res) == 1 and i== len(keys)-1:
                res.append(i+2)
        return res

s = Solution()
print s.findErrorNums([1,3,3])
print s.findErrorNums([1,3,3])