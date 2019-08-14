import itertools


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        permutations = itertools.permutations(A)
        res = (0, "")
        for h1, h2, m1, m2 in permutations:
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            time = hours * 60 + minutes
            if 0 <= hours < 24 and 0 <= minutes < 60 and time >= res[0]:
                res = (time, "{:02}:{:02}".format(hours, minutes))
        return res[1]
