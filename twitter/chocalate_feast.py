# https://www.hackerrank.com/challenges/chocolate-feast
#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    res = 0
    wrapper = 0
    for i in xrange(t):
        if i == 0: # first time
            res += n / c
            wrapper = res
        elif wrapper >= m:
            res += (wrapper / m)
            wrapper = (wrapper / m + wrapper % m)
    print res