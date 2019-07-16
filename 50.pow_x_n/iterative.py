class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n > 1:
            if n % 2 == 1:
                res *= x
            x *= x
            n >>= 1
        return res * x
