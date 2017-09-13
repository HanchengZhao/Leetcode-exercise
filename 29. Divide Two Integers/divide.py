class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxInt = 2 ** 31 - 1
        # corner case
        if divisor == 0:
            return maxInt
        if dividend == 0:
            return 0
        sign = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        c, sub = 1, divisor
        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                res += c
                sub = (sub << 1)
                c = c << 1
            else:
                sub = (sub >> 1)
                c = c >> 1
        res = res if sign == 1 else -res
        return min(maxInt, max(-maxInt-1, res)) # avoid overflow here
s = Solution()
print s.divide(-3,3)

'''
for example, if we want to calc (17/2)

ret = 0;

17-2 ,ret+=1; left=15

15-4 ,ret+=2; left=11

11-8 ,ret+=4; left=3

3-2 ,ret+=1; left=1

ret=8;

the trick to accelerate the computing is to use a sub to get the divisor, and if it is smaller than divident,
multiply it by 2 by shifting to left everytime, otherwise shift back
Long division in binary:
The outer loop reduces n by at least half each iteration. So It has O(log N) iterations.
The inner loop has at most log N iterations.
So the overall complexity is O(( log N)^2)
'''