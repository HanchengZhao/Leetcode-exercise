class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dif = x ^ y 
        count = 0
        # count 1s in dif
        while dif:
            count += dif & 1 
            dif >>= 1
        return count

        # return bin(x^y).count('1')