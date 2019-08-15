class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 1, x
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        return res
