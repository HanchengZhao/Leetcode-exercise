'''
calculator三组题
第一问：输入string 只有加减和数字，如"1+2-3"。 用一个整数存数字前面的符号。
第二问：第一问的基础上加括号，如"(1+2)-3"。用Stack存括号前面“真正”的符号, 遇到符号乘上stack.peek()
第三问：第二问的基础上加上变量，给了一部分变量对应的值，化简表达式。如"(a+b)+c+d+1", 给map {"a":1,"b":2,"c":3},输出"7+d"。用另外一个map存没有出现的变量的出现次数，其余变量or数字直接加到结果里面。

'''

# 1.


def calculator_1(s):
    sign = 1
    total = 0
    i = 0
    while i < len(s):
        char = s[i]
        if char == "+" or char == "-":
            sign = 1 if char == "+" else -1
            i += 1
        elif char.isdigit():
            val = ""
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            total += sign * int(val)
            sign = 1
        else:
            i += 1
    return total


print(calculator_1("1+2-4"))

# 2


def calculator_2(s):
    signs = [1, 1]
    total = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in "+-(":
            signs.append(signs[-1] * ((-1) if c == "-" else 1))
        elif c.isdigit():
            val = ""
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            total += signs[-1] * int(val)
            signs.pop()
            continue
        elif c == ")":
            signs.pop()
        i += 1
    return total


print(calculator_2("1+2-(3-4)"))

# 3
