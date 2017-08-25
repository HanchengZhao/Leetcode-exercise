class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1, c2 = float('inf'), float('inf')
        for i in nums:
            if i <= c1:
                c1 = i  # smallest so far (it's a candidate for 1st element)
            elif i <= c2: #   c1< i < c2
                c2 = i
            else: # here when we have/had c1 < c2 already and i > c2
                return True # the increasing subsequence of 3 elements exists
        return False