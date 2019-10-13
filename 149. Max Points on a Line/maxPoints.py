from fractions import Fraction


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxPoints = 0
        n = len(points)
        for i in range(n):
            # i for infinite, when x value of 2 points are the same
            slopes = {"i": 0}
            same = 1
            x, y = points[i][0], points[i][1]

            for j in range(i+1, n):
                nx, ny = points[j][0], points[j][1]
                if nx == x and ny == y:
                    same += 1
                elif nx == x:
                    slopes["i"] += 1
                else:
                    # use Fraction here to solve long double like test case : [[0,0],[94911151,94911150],[94911152,94911151]]
                    slope = Fraction((ny - y), (nx - x))
                    slopes[slope] = slopes.get(slope, 0) + 1
            maxPoints = max(maxPoints, max(slopes.values()) + same)
        return maxPoints


'''
idea : https://leetcode.com/problems/max-points-on-a-line/discuss/47117/Sharing-my-simple-solution-with-explanation
time: O(n^2)
'''
