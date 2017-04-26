class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []
        self.sums = 0.0
    # keep track of sums to make next run in O(1)
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.sums += val
        if len(self.queue) > self.size:
            self.sums -= self.queue.pop(0)
        return self.sums / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)