class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        # odd length
        for i in range(len(s)):
            k = 0
            while i - k >= 0 and i + k <= len(s) - 1:
                if s[i-k] == s[i+k]:
                    if 2*k + 1 > len(longest):
                        longest = s[i-k:i+k+1]
                    k += 1
                else:
                    break
        # even length
        for i in range(len(s)):
            k = 1
            while i - k + 1 >= 0 and i + k <= len(s) - 1:
                if s[i-k+1] == s[i+k]:
                    if 2*k > len(longest):
                        longest = s[i-k+1:i+k+1]
                    k += 1
                else:
                    break
        return longest
