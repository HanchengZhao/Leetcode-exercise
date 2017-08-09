import heapq
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        heapq.heappush(self.heap, x)

    def pop(self):
        """
        :rtype: void
        """
        heapq.heappop(self.heap)

    def top(self):
        """
        :rtype: int
        """
        return self.heap[0]


    def getMin(self):
        """
        :rtype: int
        """
        return heapq.nsmallest(1)[0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(3)
obj.push(2)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
