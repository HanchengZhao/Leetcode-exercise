class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        first = logs[0].split(":")
        stack.append(int(first[0])) # push the start id to stack
        i = 1 
        prev = int(first[2]) # record previous timestamp
        while i < len(logs):
            log = logs[i].split(':')
            if log[1] == 'start':
                if stack: # add time interval to last func in stack
                    res[stack[-1]] += int(log[2]) - prev
                stack.append(int(log[0]))
                prev = int(log[2])
            else: # end
                id = int(log[0])
                res[id] += int(log[2]) - prev + 1 # +1 because end at very end
                prev = int(log[2]) + 1
                stack.pop()
            i += 1
        return res
'''
Use a stack to record all start timestamps of each function, and use
a variable prev to record last log time, use 'res' to record the time executed
for every func. 
'''

            
