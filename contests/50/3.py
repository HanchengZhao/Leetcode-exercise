class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        for i in s:
            print i
            if i == "(":
                stack.append('(')
            elif i == '*':
                stack.append('*')
            else: #")"
                if not stack:
                    return False
                j = 1
                found = 0
                while j <= len(stack):
                    if stack[-j] == '(':
                        stack.pop(-j)
                        found = 1
                        break
                    j += 1
                if found == 0:
                    stack.pop()
                # pop *
                
        # if all * 
        count = 0
        for i in stack:
            if i == '(':
                count += 1
            if i == '*':
                if count > 0:
                    count -= 1
        return count == 0
s = Solution()
print s.checkValidString("(*))")