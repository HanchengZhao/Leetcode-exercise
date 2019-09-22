import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        ends = []
        rooms = 0
        for start, end in intervals:
            if not ends or start < ends[0]:
                rooms += 1
            else:
                if ends and start >= ends[0]:
                    heapq.heappop(ends)
            heapq.heappush(ends, end)
        return rooms
