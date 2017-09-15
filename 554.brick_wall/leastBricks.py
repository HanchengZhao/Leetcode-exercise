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
        least = len(wall) - max(spaceMap.values()) if spaceMap.values() else len(wall) # avoid empty spaceMap for max
        return least

s = Solution()
print s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
'''
use spacemap to record where spaces exist in each row,
key is length(col number), value is number of spaces in all rows
'''