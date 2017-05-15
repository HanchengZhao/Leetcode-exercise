from collections import defaultdict
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        dic = defaultdict(list)
        res = []
        for i, parent in enumerate(ppid):
            dic[parent].append(pid[i])
        queue = [kill]
        while queue:
            child = queue.pop()
            res.append(child)
            queue.extend(dic[child])
        return res
s = Solution()
print s.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)