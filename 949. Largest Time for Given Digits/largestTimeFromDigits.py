class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        def getPermutation(lst):
            if not lst:
                return []
            if len(lst) == 1:
                return [lst]
            l = []
            for i in range(len(lst)):
                m = lst[i]
                remainList = lst[:i] + lst[i+1:]
                for p in getPermutation(remainList):
                    l.append([m] + p)
            return l
        permutations = getPermutation(A)
        # # time, string
        res = (0, "")
        for h1, h2, m1, m2 in permutations:
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            time = hours * 60 + minutes
            if 0 <= hours < 24 and 0 <= minutes < 60 and time >= res[0]:
                # format the time, so 0:0 would be "00:00"
                res = (time, "{:02}:{:02}".format(hours, minutes))
        return res[1]
