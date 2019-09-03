'''
The basic idea would be using 2 bit masks:
  1. use the first to get the x ^ y
  2. use the second one to get one of them, say, x
  3. then we can get the y using the first mask
'''


class Solution:
    def singleNumber(self, nums):
        # we first XOR all the numbers to eliminate all the pairs
        mask1 = 0
        # mask1 will be x ^ y in the end, because all the pairs will become 0
        for num in nums:
            mask1 = mask1 ^ num
        # mask2 will contain the rightmost 1, which only exists in either x or y, let's say x,
        # but will not exist in y, so we can eliminate y in this loop
        mask2 = mask1 & (-mask1)
        x = 0
        for num in nums:
            # contains only x
            if mask2 & num:
                x = x ^ num
        y = mask1 ^ x
        return [x, y]
