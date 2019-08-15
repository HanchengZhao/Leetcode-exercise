class Solution:
    def calculate(self, s: str) -> int:
        numberstack = []
        operationstack = []
        # push number strings and operations to each stack
        numstring = ""
        for i in s:
            if i == " ":
                if numstring:
                    numberstack.append(int(numstring))
                    numstring = ""
            elif i.isnumeric():
                numstring += i
            else:
                if numstring:
                    numberstack.append(int(numstring))
                    numstring = ""
                operationstack.append(i)
        if numstring:
            numberstack.append(int(numstring))
        i = 0
        # handle "*" and "/" first
        while i < len(operationstack):
            if operationstack[i] == "*":
                numberstack = numberstack[:i] + [numberstack[i]
                                                 * numberstack[i+1]] + numberstack[i+2:]
                operationstack.pop(i)
            elif operationstack[i] == "/":
                numberstack = numberstack[:i] + [numberstack[i] //
                                                 numberstack[i+1]] + numberstack[i+2:]
                operationstack.pop(i)
            else:
                i += 1
        res = numberstack[0]
        for i, op in enumerate(operationstack):
            if op == "+":
                res += numberstack[i+1]
            if op == "-":
                res -= numberstack[i+1]
        return res
