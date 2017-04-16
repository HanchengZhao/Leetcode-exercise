class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for row in xrange(len(words)):
            for col in xrange(len(words[row])):
                if col >= len(words) or row >= len(words[col]) or words[row][col] != words[col][row]:
                    return False
        return True