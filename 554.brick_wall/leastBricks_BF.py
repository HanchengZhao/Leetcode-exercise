class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        least = len(wall)
        while wall[0] and not (wall[0][0] == 1 and len(wall[0]) == 1):
            count = 0
            for row in wall:
                if row[0] == 1:
                    row.pop(0)
                else:
                    row[0] -= 1
                    count += 1
            least = min(least, count)
        return least