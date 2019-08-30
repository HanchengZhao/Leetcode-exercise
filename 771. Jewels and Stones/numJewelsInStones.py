class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jews = set()
        count = 0
        for i in J:
            jews.add(i)
        for s in S:
            if s in jews:
                count += 1
        return count