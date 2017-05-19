class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in xrange(len(s)-1):
            if s[i] == "+" and s[i+1] == "+":
                flipped = s[0:i] + "--" + s[i+2:] if i+2 < len(s) else s[0:i] + "--"
                res.append(flipped)
        return res