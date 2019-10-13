
text = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
exclude = ['and', 'he', 'the', 'to', 'is', 'Jack', 'Jill']


def wordsToExclude(text, exclude):
    from collections import defaultdict
    wordList = set()
    for word in exclude:
        if word:
            wordList.add(word.lower())
    idx = 0
    wordCnt = defaultdict(int)
    maxCnt = 0
    while idx < len(text):
        if text[idx].isalpha():
            tmp = idx
            while text[tmp].isalpha():
                tmp += 1
            word = text[idx:tmp].lower()
            if word not in wordList:
                wordCnt[word] += 1
                maxCnt = max(maxCnt, wordCnt[word])
            idx = tmp + 1
        else:
            idx += 1
    ret = []
    for word in wordCnt:
        if wordCnt[word] == maxCnt:
            ret.append(word)
    return ret


print(wordsToExclude(text, exclude))
