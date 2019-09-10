from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()
        self.hitscount = {}
        self.total = 0

    def _removeFrom(self, timestamp):
        while self.hits and self.hits[0] <= timestamp - 300:
            last = self.hits.popleft()
            self.total -= self.hitscount[last]
            del self.hitscount[last]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.hits and self.hits[-1] == timestamp:
            self.hitscount[timestamp] += 1
        else:
            self.hits.append(timestamp)
            self.hitscount[timestamp] = 1
        self.total += 1
        self._removeFrom(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self._removeFrom(timestamp)
        return self.total


'''
Use a double-ended queue to keep track of the timestamps.
time:
  hit: O(s), s = 300
  getHits: O(s), s = 300
'''
