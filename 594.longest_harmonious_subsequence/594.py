from collections import OrderedDict
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = OrderedDict()
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        keys = sorted(dic.keys())
        res = 0
        for i in xrange(len(keys)-1):
            print keys[i], keys[i+1]
            if keys[i] == keys[i+1]-1:
                res = max(dic[keys[i+1]] + dic[keys[i]], res)
        return res
s = Solution()
print s.findLHS([1,3,2,2,5,2,3,7,3])
