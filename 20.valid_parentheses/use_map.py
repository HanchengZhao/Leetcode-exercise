class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for i in s:
            if i in pairs:
                if len(stack) > 0 and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
            else:  # open chars
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
# use a pairs map for faster lookup
