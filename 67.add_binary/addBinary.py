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
            return a;
        a_2 = int(a,2) # convert binary number to decimal
        b_2 = int(b,2)
        carry = 1
        while carry:
            carry = (a_2 + b_2) << 1
            a_2 = a_2 ^ b_2
            b_2 = carry
        return bin(a_2)[2:]