from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if self.isValid(s): # check empty or already valid string
            return [s]
        queue = deque([s])
        visited = {s}
        res = []
        found = False
        while queue:
            comb = queue.popleft()
            if self.isValid(comb):
                res.append(comb)
                found = True
                
            if found:
                continue # this will skip next part but pop out all str in queue
            for i in xrange(len(comb)):
                if comb[i] == "(" or comb[i] == ")": # only deals with parenthesis
                    newcomb = comb[:i] + comb[i+1:]
                    if newcomb not in visited:
                        queue.append(newcomb)
                        visited.add(newcomb) # don't for get this
        return res
    def isValid(self, s):
        count = 0
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
                if count < 0:
                    return False # ')' can not come first
        return count == 0
