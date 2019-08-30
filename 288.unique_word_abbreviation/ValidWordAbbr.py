class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dic = {}
        for w in dictionary:
            if len(w) <= 2:
                self.dic[w] = w
            else:
                abbr = self.getAbbr(w)
                if abbr not in self.dic:
                    self.dic[abbr] = w
                else:
                    self.dic[abbr] = 2

    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            return True
        abbr = self.getAbbr(word)
        if abbr not in self.dic:
            return True
        elif self.dic[abbr] == word:
            return True
        else:
            return False

    def getAbbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]
