class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # grayCode is symmetric
        # each time you want to expand to one more digit, just add 0 on the left for each element
        # in the array and add 1 for the reversed array to keep symmetric
        res = [0]
        for i in xrange(n):
            for element in res[::-1]:
                res.append(2 ** i + element)
        return res
s = Solution()
print s.grayCode(0)