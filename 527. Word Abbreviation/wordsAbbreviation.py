from collections import defaultdict


class Solution:
    def wordsAbbreviation(self, dic: List[str]) -> List[str]:
        res = ["" for i in range(len(dic))]
        abbrs = defaultdict(list)
        for i, w in enumerate(dic):
            # handle short words
            if len(w) <= 3:
                res[i] = w
            # build a map to store previous abbrevation and index
            else:
                abbr = self.genAbbr(w, 1)
                abbrs[abbr] = (w, i)
        for abb in abbrs.keys():
            if len(abbrs[abb]) == 1:
                res[abbrs[abb][0][1]] = abb
            else:
                # handle the same abbrevation problem
                dups = abbrs[abb]
                l = len(dups[0][0])
                for i in range():
                    for j, val in enumerate(dups):

    def genAbbr(self, word, startIndex):
        return word[:startIndex] + str(len(word[startIndex:]) - 1) + word[-1]
