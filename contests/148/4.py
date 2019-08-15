class Solution:
    def longestDecomposition(self, text: str) -> int:
        if len(text) == 1:
            return 1
        start = 0
        end = len(text) - 1
        i, j = 0, len(text) - 1
        count = 1
        while i < j:
            if text[start: i+1] == text[j: end+1]:
                if i == j - 1:
                    count += 1
                else:
                    count += 2
                start = i + 1
                i += 1
                end = j - 1
                j -= 1
            else:
                i += 1
                j -= 1
        return count


s = Solution()

print(s.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
print(s.longestDecomposition("merchant"))
print(s.longestDecomposition("antaprezatepzapreanta"))
print(s.longestDecomposition("aaa"))
print(s.longestDecomposition("elvtoelvto"))
print(s.longestDecomposition("aaaa"))
