'''
For each height, we need to find its left bound and right bound.
We keep a increasing stack here, with the element index
- whenever we meet a number smaller than
  the top of the stack, which means that we found the left and right bound of the element 
  on the top of the stack, so we pop it and calculate the area with its height and width.
  width is the 
- if we meet a number larger than the top of stack, we push it.
'''


class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        # (index, val)
        stack = [(-1, 0)]
        maxArea = 0
        for i in range(len(heights)):
            while heights[i] < stack[-1][1]:
                top = stack.pop()
                # height and width
                area = top[1] * (i - stack[-1][0] - 1)
                maxArea = max(area, maxArea)
            stack.append((i, heights[i]))
        # now we only have an increasing stack
        # rightBound would be fixed to the index of last element in the stack + 1
        rightBound = stack[-1][0] + 1
        while len(stack) > 1:
            top = stack.pop()
            area = top[1] * (rightBound - stack[-1][0] - 1)
            maxArea = max(area, maxArea)
        return maxArea


# time : O(n)
# space: O(n)
# keywords: stack, array, area
