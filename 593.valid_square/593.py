class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        the basic idea is to go from every point, generate 3 lines
        that are formed with other 3 points, check whether there are
        2 lines with same length and the other one being 2 ^ 1/2 as long
        """
        def vaild(p1, p2, p3, p4):
            # from p1
            dis12 = (p1[0] - p2[0]) **2 + (p1[1] - p2[1]) **2
            dis13 = (p1[0] - p3[0]) **2 + (p1[1] - p3[1]) **2
            dis14 = (p1[0] - p4[0]) **2 + (p1[1] - p4[1]) **2
            if dis12 == dis13 and dis14 == 2* dis12 or dis12 == dis14 and dis13 == 2* dis12 or dis13 == dis14 and dis12 == 2* dis13:
                return True
            else:
                return False
        return vaild(p1, p2, p3, p4) and vaild(p2, p1, p3, p4) and vaild(p3, p2, p1, p4) and vaild(p4, p2, p3, p1)
s = Solution()
print s.validSquare([0,0],[1,1],[1,0],[0,1])
print s.validSquare([0,0],[1,1],[2,0],[0,2])
