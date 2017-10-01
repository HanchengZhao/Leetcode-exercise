def minimumMoves(a, b):
    '''
    Minimum Moves，一个整数变成另一个整数需要多少步，比如143到333需要143->243->343->333需要3步，设定输入的位数是相同的。
    '''
    res = 0
    while a:
        mod1 = a % 10
        mod2 = b % 10
        b /= 10
        a /= 10
        res += abs(mod1 - mod2)
    return res
print minimumMoves(143, 333)