from itertools import groupby
from collections import Counter

'''
There are only 2 cases that we need to take care of:
    - extend the group by 1
    - merge 2 adjacent groups together, which are only separated by 1 charactor
'''


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        group = [[k, len(list(v))] for k, v in groupby(text)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        count = Counter(text)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(l+1, count[k]) for k, l in group)
        # merge 2 groups together
        for i in range(1, len(group) - 1):
            # if both sides have the same char and are separated by only 1 char
            if group[i-1][0] == group[i+1][0] and group[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(group[i-1][1] +
                                   group[i+1][1] + 1, count[group[i-1][0]]))
        return res
