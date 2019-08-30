class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        if len(word) < len(abbr):
            return False
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isnumeric():
                # no leading 0
                if abbr[j] == "0":
                    return False
                # get the whole number
                k = j
                while k < len(abbr) and abbr[k].isnumeric():
                    k += 1
                num = int(abbr[j:k])
                # i skip num chars
                i += num
                j = k
            else:
                return False
        return i == len(word) and j == len(abbr)
