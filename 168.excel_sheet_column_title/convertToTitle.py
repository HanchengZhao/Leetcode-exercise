import math
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        '''
        eg. 52 = 26^1 * 1 + 26^0 * 26
        '''
        title = ""
        log = math.floor(math.log(n))
        for i in xrange(log,-1,-1):
            if i == 0 and n == 26:
                title += "Z"
            else:
                num = n / (26^i)
                title += chr(num - 64)
        return title


        #one liner
        #return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))
