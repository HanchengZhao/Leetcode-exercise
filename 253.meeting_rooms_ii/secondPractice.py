import heapq
class interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    def minmumMeetingRooms(self, intervals):
        intervals = sorted(intervals, key = lambda x: x.start) # has to sort because we have to pick interval in chronological order
        h = []
        rooms = 0
        for i in intervals:
            if h:
                if i.start < h[0]:
                    rooms += 1
                else:
                    heapq.heappop(h) # pop the earlist time
                heapq.heappush(h, i.end)
            else: # h is empty
                rooms += 1
                heapq.heappush(h, i.end)
        return rooms