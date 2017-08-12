# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        rooms = 1
        intervals = sorted(intervals, key = lambda x: x.start)
        h = []
        heapq.heappush(h, intervals[0].end)
        for i in xrange(1,len(intervals)):
            meeting = intervals[i]
            if meeting.start >= h[0]:
                heapq.heappop(h)
                heapq.heappush(h, meeting.end)
            else: # overlap
                heapq.heappush(h, meeting.end)
                rooms += 1
        return rooms
'''
we build a heap to track the end time for each meeting, we only need to compare the min end time with the 
new meeting start time and decide whether we need a new room
'''
