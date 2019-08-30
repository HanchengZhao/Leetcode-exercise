class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        almost same idea as 78.subsets, just to sort the list and check whether
        already in result everytime to remove duplicates
        '''
        if not nums:
            return [[]]
        nums.sort()
        res = [[]]
        index = 0
        while index < len(nums):
            nextarray = []
            for i in res:
                if (i + [nums[index]]) not in res:
                    nextarray.append(i + [nums[index]])
            res +=  nextarray
            index += 1
        return res

s = Solution()
print s.subsetsWithDup([4,4,4,1,4])

# [4,4,4,1,4]

class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for i in nums:
            for j in res[:]:
                if ([i] + j) not in res:
                    res += [[i] + j]
        return res
        