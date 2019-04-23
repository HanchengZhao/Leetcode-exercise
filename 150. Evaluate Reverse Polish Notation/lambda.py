class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "/": lambda a, b: int(a/b),  # convert float to int
            "*": lambda a, b: a*b
        }
        stack = []
        for i in tokens:
            if i in operators:
                a = stack.pop()
                b = stack.pop()
                res = operators[i](b, a)  # put the previous one first
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]
