class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        stack = []
        for i in nums:
            # stack will store elements in a decreasing order
            while not stack and stack[-1] < i:
                dic[stack.pop()] = i
            stack.append(i)
        for j in xrange(len(findNums)):
            findNums[j] = dic.get(findNums[j],-1)
        return findNums


