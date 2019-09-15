'''
We can loop through all the bitmasks instead of every words. Because there might be duplicate in
bitmasks.
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lens = {}
        for i, w in enumerate(words):
            bitmask = 0
            for char in w:
                bitmask = bitmask | (1 << (ord(char) - ord("a")))
            lens[bitmask] = max(lens.get(bitmask, 0), len(w))
        keys = lens.keys()
        longest = 0
        for i in keys:
            for j in keys:
                if not i & j:
                    longest = max(lens[i] * lens[j], longest)
        return longest
