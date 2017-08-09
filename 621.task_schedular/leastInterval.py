from collections import deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskRunner = deque(maxlen=n)
        dic = dict()
        for i in tasks: # count occurrance
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        count = 0
