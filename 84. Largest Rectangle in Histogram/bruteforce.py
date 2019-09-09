class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            minHeight = heights[i]
            for j in range(i, -1, -1):
                if heights[j] < minHeight:
                    minHeight = heights[j]
                area = minHeight * (i-j+1)
                # print(area, minHeight, i, j)
                maxArea = max(area, maxArea)
        return maxArea


'''
It takes O(n^2) for get the area
'''
