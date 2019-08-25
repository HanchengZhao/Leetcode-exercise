from collections import Counter


class Solution:
    def numSmallerByFrequency(self, queries, words):

        def calf(word):
            smallest = "z"
            for char in word:
                if char < smallest:
                    smallest = char
            return word.count(smallest)
        res = [0] * len(queries)
        queries_freq = [calf(i) for i in queries]
        words_freq = [calf(i) for i in words]
        for i, q in enumerate(queries_freq):
            count = 0
            for w in words_freq:
                if w > q:
                    count += 1
            res[i] = count
        return res


s = Solution()
print(s.numSmallerByFrequency(["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"],
                              ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]))
