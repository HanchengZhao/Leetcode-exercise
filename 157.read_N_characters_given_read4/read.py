# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while n > 0:
            buf4 = [""] * 4
            l = read4(buf4)
            if not l: # if no more char in file in 
                return idx
            for i in xrange(min(l, n)): # 
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx
'''
the idea is to extend read4 api to readn, so the funciton should be the same,
buf should be a cache and the function should return the length
'''