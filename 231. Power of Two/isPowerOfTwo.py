class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and n & (n-1) == 0
# if a number is the power of 2, it will only have one 1 on its binary
# such as 4(100), 8(1000), 16(10000)
