class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        dic = {}
        word = ""
        most, freq = "", 0
        for i in paragraph:
            if i.isalpha():
                word += i
            else:
                if word and word not in banned:
                    dic[word] = dic.setdefault(word, 0) + 1
                    if dic[word] > freq:
                        most, freq = word, dic[word]
                word = ""
        if word and word not in banned:
            dic[word] = dic.setdefault(word, 0) + 1
            if dic[word] > freq:
                most = word
        return most
