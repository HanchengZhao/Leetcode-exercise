# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = [] # used to save all the char fetched

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while True:
            buf4 = [""] * 4 # defines the size of return array, otherwise index out of range, contain the return chars, it is the destination, not the source
            l = read4(buf4) # return the length, read4() function will go to the file and fetch chars
            self.queue.extend(buf4)
            leftnum = min(len(self.queue), n - idx) # number of chars left
            for i in xrange(leftnum):
                buf[idx] = self.queue.pop(0)
                idx += 1
            if leftnum == 0: # reach the end
                break
        return idx