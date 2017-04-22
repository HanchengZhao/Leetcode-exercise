# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        #init
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        res = []
        pos = 0
        #traverse the list, merge if overlapping
        for inter in intervals:
            if inter.end < newInterval.start:
                res.append(inter)
                pos += 1
            elif inter.start > newInterval.end:
                res.append(inter)
            else:
                newInterval.start = min(inter.start, newInterval.start)
                newInterval.end = max(inter.end, newInterval.end)
        res.insert(pos, newInterval)
        return res


#time: O(n)
#space: O(1)
