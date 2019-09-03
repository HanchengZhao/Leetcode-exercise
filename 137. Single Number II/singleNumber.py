class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we need to use 2 bit masks to make sure
        # we don't record nums that appear 3 times
        seen_once = seen_twice = 0
        for num in nums:
            # we only append to seen_once if the number is not in seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            # we only append to see_twice if the number is not in seen_once
            seen_twice = ~seen_once & (seen_twice ^ num)
        # in the end, we only have element that appears once in the seen_once
        return seen_once
