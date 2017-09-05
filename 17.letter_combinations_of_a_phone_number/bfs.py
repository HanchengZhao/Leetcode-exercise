from collections import deque
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping=[[''],['_'],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        queue = deque()
        queue.append("")
        for i in digits:
            for j in xrange(len(queue)):
                last = queue.popleft()
                for k in mapping[int(i)]:
                    queue.append(last + k)
        return list(queue)

'''
bfs solution avoids the entire copy of the last res
'''
s = Solution()
print s.letterCombinations('23')