class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0] * 26
        for i in tasks:
            count[ord(i) - ord('A')] += 1
        count.sort()
        maxVal = count[-1]
        idleSlot = n * (maxVal-1)
        i = 24
        while i >= 0 and count[i] > 0:
            idleSlot -= min(count[i], maxVal-1) # should be smaller than maxVal-1
            i -= 1
        return idleSlot + len(tasks) if idleSlot > 0 else len(tasks)
'''
so the basic idea is to execute the most frequent task first, then count fixed
idle slots between it. Then check if the rest tasks can fit into slot. In the end
idle slot could be negative in this way(e.g n == 0), so it is either length of task
or the length plus positive idle slot number

time : O(n), loop over task using O(n), sorting takes O(26log(26)) = O(1)
'''