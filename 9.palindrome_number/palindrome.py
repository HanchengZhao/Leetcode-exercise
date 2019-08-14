class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        orig = x
        w = 0
        factor = 0
        while x > 0:
            w = w * 10 + x % 10
            x = x // 10
            factor += 1
        return w == orig
