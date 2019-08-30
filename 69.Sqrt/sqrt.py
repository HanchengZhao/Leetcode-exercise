class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def bs(lo, hi):
            if lo+1 == hi: 
                return lo
            mid = (lo+hi)/2
            if mid * mid < x:
                return bs(mid, hi)
            if mid * mid > x:
                return bs(lo, mid)
            else:
                return mid
        return bs(1, x)