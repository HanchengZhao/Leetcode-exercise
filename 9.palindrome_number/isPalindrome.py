class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # reverse the last half of digits and compare 
        # based on odd or even number of digits
        if x < 0 or (x != 0 and x % 10 == 0) : #least significant digit is 0
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x /= 10
        # even or odd
        # like '12344321' or '123454321
        return x == reverse or x == reverse / 10
s = Solution()
s.isPalindrome(3)