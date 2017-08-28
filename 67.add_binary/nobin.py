class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        if len(a) <= len(b): # let a be the longer one
            a, b = b, a
        carry = 0
        res = ''
        for i in xrange(1, len(b)+1): # add both digit on b
            digit = (int(b[-i]) + int(a[-i]) + carry) % 2
            carry = (int(b[-i]) + int(a[-i]) + carry) / 2
            res = str(digit) + res
        for j in xrange(len(b)+1, len(a)+1): # add exclusive digit on a
            digit = (int(a[-j]) + carry) % 2
            carry = (int(a[-j]) + carry) / 2
            res = str(digit) + res
        if carry == 1: # do not forget the left one
            res = str(carry) + res
        return res