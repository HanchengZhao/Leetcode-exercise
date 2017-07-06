class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum, mask = 0, 0
        # start from the most significant digit
        # and see if there are pairs that have different values on that
        # digit
        for i in xrange(31, -1, -1):
            mask = mask | (1 << i)
            s = set()
            for num in nums:
                s.add(num & mask) # store the different result in terms of most significant digits
            temp = maximum | (1 << i)
            for prefix in s:
                if temp ^ prefix in s:
                    maximum = temp
                    break
        return maximum
