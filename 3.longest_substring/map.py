class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # index of last occurance
        dic = {}
        longest = 0
        start = 0
        for i, val in enumerate(s):
            if val not in dic:
                dic[val] = i
            else:
                start = max(dic[val] + 1, start)
                dic[val] = i
            longest = max(longest, i-start+1)
        return longest
