def isnumber(s):
    # space, dot, e, sign,
    num = False
    numAfterE= True
    dot = False
    exp = False
    sign = False
    s.strip()
    for i, val in enumerate(s):
        if val == ' ': # should not have space inbetween
            return False
        elif val == '.':
            if exp and dot:
                return False
            dot = True
        elif val == 'e':
            if exp or not num:
                return False
            exp = True
        elif val == '+' or '-':
            if i != 0 or s[i-1] != 'e':
                return False
            sign = True
        elif val.isdigit():
            num = True
            numAfterE = True
        else:
            return False
        return num and numAfterE