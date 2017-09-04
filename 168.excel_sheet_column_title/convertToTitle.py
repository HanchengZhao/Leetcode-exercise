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
        if n == 0:
            return ""
        right = chr((n - 1) % 26 + ord('A'))
        return self.convertToTitle((n - 1) / 26) + right


        #one liner
        #return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))
