'''
if the requirement is keeping the task order
'''
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = {}
        cur = 0 # current position in the task line
        for i in tasks:
            if i not in map:
                map[i] = cur + n + 1 # save cool time
                cur += 1
            else: 
                if cur < map[i]:
                    cur += (map[i] - cur + 1) # map[i] - cur for slots and 1 for itself
                else:
                    cur += 1
                map[i] = cur + n# update
        return cur
s = Solution()
print s.leastInterval(['A','A','A','B','B','B'],2)
print s.leastInterval(['A','B','A','B','A','B'],2)
print s.leastInterval(['A','A'],2)
