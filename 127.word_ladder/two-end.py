class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        wordDict = set(wordDict)
        if endWord not in wordDict:
            return 0
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordDict.discard(beginWord)
        while front:
            # generate all valid transformations
            front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
        return 0
if __name__ == '__main__':
    s = Solution()
