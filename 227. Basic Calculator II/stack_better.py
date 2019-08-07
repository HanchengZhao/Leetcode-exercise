class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack, numstring, op = [], "", "+"
        for i in range(len(s)):
            if s[i].isdigit():
                numstring += s[i]
            # is an operation string or reach the end
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if op == "+":
                    stack.append(int(numstring))
                elif op == "-":
                    stack.append(-int(numstring))
                elif op == "*":
                    stack.append(stack.pop() * int(numstring))
                else:
                    # -3 / 2  should be -1, but it's -2 in python3
                    tmp = stack.pop()
                    nxt = int(numstring)
                    # only happens for negative odd
                    if tmp // nxt < 0 and tmp % nxt != 0:
                        stack.append(tmp // nxt + 1)
                    else:
                        stack.append(tmp // nxt)
                numstring = ""
                op = s[i]
        return sum(stack)
