import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []
        self.higher = []
        heapq.heapify(self.lower)
        heapq.heapify(self.higher)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.lower and -self.lower[0] < num:
            heapq.heappush(self.higher, num)
        else:
            heapq.heappush(self.lower, -num) #maxheap

        #rebalance
        if len(self.lower) - len(self.higher) > 1:
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
        elif len(self.higher) - len(self.lower) > 1:
            heapq.heappush(self.lower, -heapq.heappop(self.higher))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lower) == len(self.higher):
            if not self.lower:
                return 0.0
            return float(-self.lower[0] + self.higher[0]) / 2
        elif len(self.lower) > len(self.higher):
            return float(-self.lower[0])
        elif len(self.lower) < len(self.higher):
            return float(self.higher[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# print obj.findMedian()
# obj.addNum(1)
# print obj.findMedian()
# obj.addNum(2)
# print obj.findMedian()
# obj.addNum(3)
# obj.addNum(4)
# print obj.findMedian()
# print obj.lower, obj.higher