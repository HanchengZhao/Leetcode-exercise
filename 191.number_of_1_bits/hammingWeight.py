class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = n
        count = 0
        while bits:
            if bits & 1:
                count += 1
            bits = bits >> 1
        return count