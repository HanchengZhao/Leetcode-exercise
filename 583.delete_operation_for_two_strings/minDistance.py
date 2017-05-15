class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #find the longest common sequence
        dp = [[0] * (len(word1) + 1) for i in xrange(len(word2) + 1)]
        for i in xrange(len(word2)):
            for j in xrange(len(word1)):
                if word1[j] == word2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1 # comment1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        lgst = dp[len(word2)][len(word1)]
        return len(word1) - lgst + len(word2) - lgst
s = Solution()
print s.minDistance("food", "money")
'''
comment1:
previously dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]) + 1
this will cause a problem that the same character will be matched twice,
so whenever there is a match, both indexes have to go forward
'''
