class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        count = 0
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
            if dic[c] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1
'''
single pass
'''