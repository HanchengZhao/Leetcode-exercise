'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
'''


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, low = 0, 0
        dic = {}
        for i in xrange(len(s)):
            dic[s[i]] = i
            if len(dic) > k:
                low = min(dic.values())
                del dic[s[low]]
                low += 1
            res = max(res, i - low + 1)
        return res


'''
Time complexity of this is O(nk), because it takes O(k) to find the low index
'''
