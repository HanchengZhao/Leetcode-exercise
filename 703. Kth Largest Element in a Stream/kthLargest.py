import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums[:]
        self.k = k
        heapq.heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappop(self.h)
            heapq.heappush(self.h, val)
        return self.h[0]
# use a min-heap to keep kth largest elements
# time: O(n * klog(k))
