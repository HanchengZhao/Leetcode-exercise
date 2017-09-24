'''
abc9 < abc123 abc > ab9 
'''
def stringComparator(s1, s2):
    if not s2:
        return 1 # s1 is bigger
    if not s1:
        return -1
    i1, i2 = 0, 0
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1].isdigit() and s2[i2].isdigit(): # both are integers
            j1 = i1 + 1
            j2 = i2 + 1
            while j1 < len(s1) and s1[j1].isdigit():
                j1 += 1
            while j2 < len(s2) and s2[j2].isdigit():
                j2 += 1
            if int(s1[i1:j1]) > int(s2[i2:j2]):
                return 1
            elif int(s1[i1:j1]) < int(s2[i2:j2]):
                return -1
            else: # equal
                i1 = j1
                i2 = j2
        elif s1[i1].isdigit(): # i1 is char
            return -1
        elif s2[i2].isdigit(): # i2 is char
            return 1
        else: # both are char
            if ord(s1[i1]) > ord(s2[i2]):
                return 1
            elif ord(s1[i1]) < ord(s2[i2]):
                return -1
            else: # equal
                i1 += 1
                i2 += 1
    return 1 if i2 == len(s2) else -1
print stringComparator('abc9', 'abc123') # -1
print stringComparator('abc9', 'abc1') # 1
print stringComparator('abc9', 'ab2') # 1
print stringComparator('abc', 'abcd') # -1 
        

