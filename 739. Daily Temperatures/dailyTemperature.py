# use a stack to keep track of days that have no higher temperature yet
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i, val in enumerate(T):
            while stack and val > stack[-1][0]:
                last = stack.pop()
                res[last[1]] = i - last[1]
            stack.append((val, i))
        return res
