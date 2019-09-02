'''
For optimization, We don't need to count the charactor, we only need to record
whether we have odd or even number of this char, thus using 0 or 1 to represent on this digit.
'''


class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        N = 26
        # get the index value of each char in s
        ints = list(map(lambda c: ord(c) - ord("a"), s))
        S = len(s)
        dp = [0] * (S + 1)
        for i in range(1, S+1):
            # use XOR to get the odd/even number on that index
            dp[i] = dp[i-1] ^ (1 << ints[i-1])
        res = []
        for l, r, k in queries:
            # bin converts an integer number to a binary string
            ones = bin(dp[r+1] ^ dp[l]).count("1")
            res.append(ones >> 1 <= k)
        return res
