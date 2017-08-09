from collections import defaultdict
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for i in words:
