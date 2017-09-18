# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while n:
            buf4 = [""] * 4
            l = read4(buf4)
            self.queue.extend(buf4)
            if len(self.queue) == 0:
                return index
            for i in xrange(min(n, len(self.queue))):
                buf[index] = self.queue.pop(0)
                index += 1
                n -= 1
        return index
'''
the difference between 158 and 157 is that read function in
158 could be called multiple times, so we need save all
characters left from last call in a queue
'''