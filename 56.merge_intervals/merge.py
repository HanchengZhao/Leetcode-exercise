# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) ==  0: return []
        #sort the start point first
        intervals = sorted(intervals, key = lambda x : x.start)
        res = [intervals[0]]
        #if there is overlap, merge 2 intervals; otherwise append to list
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res.append(intervals[i])
        return res