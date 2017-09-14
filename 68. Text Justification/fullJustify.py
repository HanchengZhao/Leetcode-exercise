class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return ['']
        i = 0
        wordsThisLevel = ""
        res = []
        # allocate space
        while i < len(words):
            # decide how many words we should use
            if (len(wordsThisLevel) + len(words[i])) <= maxWidth:
                wordsThisLevel += words[i] + " " # this could be bigger than 16
            else:
                for j in xrange(len(wordsThisLevel)):
                    if wordsThisLevel[j] == ' ' and len(wordsThisLevel) < maxWidth:
                        wordsThisLevel = wordsThisLevel[:j] + ' ' + wordsThisLevel[j:]
            