from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if not s:
            return [""]
        visited = {s} # a set to store all visited states
        queue = deque([s]) # store every combination 
        found = False
        while queue:
            string = queue.popleft()
            if self.isValid(string):
                res.append(string)
                found = True
            
            if found:
                continue # skip next loop
            for i in xrange(len(string)):
                if string[i] == "(" or string[i] == ")":
                    s = string[:i] + string[i+1:]
                    if s not in visited:
                        queue.append(s)
                        visited.add(s)
        if len(res) == 0:
            return [""]
        return res
                
    def isValid(self, s):
        count = 0
        for i in xrange(len(s)):
            if s[i] == "(":
                count += 1
            if s[i] == ")": 
                if count <= 0: # ')' could not be the leading parentheses
                    return False
                count -= 1
        return count == 0
'''
use bfs to remove every "(" or ")" for testing
the bfs solution will make sure the array of valid strings that are found first are shortest
'''