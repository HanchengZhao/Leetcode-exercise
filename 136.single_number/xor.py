# if a number XOR itself, we get 0
# but any number xor 0 would be itself


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for n in nums:
            x = x ^ n
        return x
