class Solution:
    def longestWord(self, words):
        words.sort()
        dic = {}
        longest = ""
        for w in words:
            root = dic
            for i, char in enumerate(w):
                if char in root:
                    root = root[char]
                else:
                    # reach the end
                    if i == len(w)-1:
                        root[char] = {}
                        if len(w) > len(longest):
                            longest = w
                    else:
                        break
        return longest
