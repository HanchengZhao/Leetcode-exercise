def generateP(n):
    res = []
    traverse(res, '', 0, 0, n)
    return res
def traverse(res, path, open, close, max):
    if len(path) == max * 2:
        res.append(path)
    if open < max:
        traverse(res, path + '(', open + 1, close, max)
    if close < max:
        traverse(res, path + ')', open, close + 1, max)

print generateP(2)