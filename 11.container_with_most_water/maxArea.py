class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        Max = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            Max = max(area, Max)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return Max
