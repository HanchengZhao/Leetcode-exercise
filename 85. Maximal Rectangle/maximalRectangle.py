'''
The same idea as leetcode84, but we calculate histogram from each row
so the time complexity would be O(n * m), row * col
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        def maxAreaHistogram(heights):
            stack = [(-1, 0)]
            maxArea = 0
            for i in range(len(heights)):
                while heights[i] < stack[-1][1]:
                    top = stack.pop()
                    area = top[1] * (i - stack[-1][0] - 1)
                    maxArea = max(maxArea, area)
                stack.append((i, heights[i]))
            rightbound = stack[-1][0] + 1
            while len(stack) > 1:
                top = stack.pop()
                area = top[1] * (rightbound - stack[-1][0] - 1)
                maxArea = max(maxArea, area)
            return maxArea

        m, n = len(matrix), len(matrix[0])
        heights = [0 for _ in range(n)]
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = maxAreaHistogram(heights)
            maxArea = max(maxArea, area)
        return maxArea
