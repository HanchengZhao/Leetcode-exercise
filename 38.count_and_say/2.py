class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in xrange(n-1):
            temp = ''
            count = 1
            for j, val in enumerate(res):
                if j < len(res)-1 and val == res[j+1]: # duplicate
                    count += 1
                else: # add and recover
                    temp += str(count) + val
                    count = 1
            res = temp
        return res