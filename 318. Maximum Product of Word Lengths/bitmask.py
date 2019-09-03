'''
use bitmasks to check if 2 words have the same charactors
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        lens = [0] * n
        for i, w in enumerate(words):
            bitmask = 0
            for char in w:
                bitmask = bitmask | 1 << (ord(char) - ord("a"))
            bitmasks[i] = bitmask
            lens[i] = len(w)
        longest = 0
        for i in range(n):
            for j in range(n):
                if not bitmasks[i] & bitmasks[j]:
                    longest = max(longest, lens[i] * lens[j])
        return longest
