class Solution:
# @param n, an integer
# @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res += 1 & n
            if i == 31:
                return res
            n >>= 1
            res <<= 1

s = Solution()
print s.reverseBits(43261596)