'''
Because we can rearrange the substring, so we only need to record the 
occurrance of each charactors. 

In order to optimize, we can calculate the prefix sum of each substring first,
we can use an int array to record 26 charactors' count.
'''


class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        N = 26
        # init the
        prefix = [[0] * 26]
        for char in s:
            nextCount = prefix[-1][:]
            nextCount[ord(char) - ord("a")] += 1
            prefix.append(nextCount)
        res = []
        for l, r, k in queries:
            right = prefix[r+1]
            left = prefix[l]
            # get the odd count on each char
            odds = sum([(right[i] - left[i]) & 1 for i in range(26)])
            # we only need to eliminate half odds
            res.append((odds >> 1) <= k)
        return res
