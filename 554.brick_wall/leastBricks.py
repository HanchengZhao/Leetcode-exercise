class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        spaceMap = dict()
        for row in wall:
            spacelen = 0
            for brick in row[:-1]: # avoid counting wall edge
                spacelen += brick
                if spacelen not in spaceMap:
                    spaceMap[spacelen] = 1
                else:
                    spaceMap[spacelen] += 1
        least = len(wall) - max(spaceMap.values())
        return least

s = Solution()
print s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])