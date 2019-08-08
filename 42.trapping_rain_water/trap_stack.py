'''
The basic idea is to use a stack to keep track of the previous lower bound

'''


class Solution:
    def trap(self, height: List[int]) -> int:
        res, i = 0, 0
        stack = []
        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:  # we don't have left boundary
                    break
                distance = i - stack[-1] - 1
                boundHeight = min(height[i], height[stack[-1]]) - height[top]
                res += distance * boundHeight
            stack.append(i)
            i += 1
        return res
