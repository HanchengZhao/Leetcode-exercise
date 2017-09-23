'''
"(a)()" -> "(a)()"
"((bc)" -> "(bc)"
")))a((" -> "a"
"(a(b)" ->"(ab)" or "a(b)"
'''

def balanceParenthesis(s):
    l, r = 0, 0
    lscan = []
    rscan = []
    for i in s:
        if i == '(':
            l += 1 
            lscan.append('(')
        elif i == ')':
            if l > 0: # has match '(' before it
                l -= 1
                lscan.append(')')
        else:
            lscan.append(i)
    for i in lscan[::-1]:
        if i == ')':
            r += 1
            rscan.append(')')
        elif i == '(':
            if r > 0:
                r -= 1
                rscan.append('(')
        else:
            rscan.append(i)
    return ''.join(rscan[::-1])
print balanceParenthesis("(a(b)")
'''
 2 rounds of scans with a counter on open parens first and one with a counter on close parens. The first scan finds all unmatched close parens and the second one finds all unmatched open parens
'''