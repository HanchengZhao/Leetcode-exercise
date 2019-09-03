class Solution:
    def maxProduct(self, words: List[str]) -> int:
        longest = 0
        for w1 in words:
            s = set()
            for char in w1:
                s.add(char)
            for w2 in words:
                hasSameChar = False
                for char in w2:
                    if char in s:
                        hasSameChar = True
                        break
                if not hasSameChar:
                    longest = max(longest, len(w1) * len(w2))
        return longest
