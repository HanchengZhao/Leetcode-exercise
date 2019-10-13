class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n-1):
            # ends with each char
            a2 = (e + i + u) % MOD
            e2 = (a + i) % MOD
            i2 = (e + o) % MOD
            o2 = i % MOD
            u2 = (i + o) % MOD
            a, e, i, o, u = a2, e2, i2, o2, u2
        return (a + e + i + o + u) % MOD


s = Solution()
print(s.countVowelPermutation(5))
