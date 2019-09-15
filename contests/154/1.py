from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text):
        c = Counter(text)
        bcount = c.get("b", 0)
        acount = c.get("a", 0)
        lcount = c.get("l", 0)
        ocount = c.get("o", 0)
        ncount = c.get("n", 0)
        # print(bcount, acount, lcount, ocount, ncount)
        return min(bcount, acount, lcount // 2, ocount // 2, ncount)


s = Solution()
print(s.maxNumberOfBalloons("loonbalxballpoon"))
