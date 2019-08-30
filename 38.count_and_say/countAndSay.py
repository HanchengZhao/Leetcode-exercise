class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        res = '1'
        for i in xrange(1, n):
            j = 0
            temp = ''
            count = 1
            while j < len(res):
                if j+1 < len(res) and res[j] == res[j+1]: # duplicate numbers
                    count += 1
                else:
                    temp += str(count) + res[j]
                    count = 1 # recover
                j += 1
            res = temp
        return res
s = Solution()
print s.countAndSay(6)