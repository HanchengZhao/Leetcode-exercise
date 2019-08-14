class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        self.helper(num, target, "", 0, 0)
        return self.res

    def helper(self, num, target, tmp, currRes, prevNum):  # currRes stores the current result, prevNum stores last added or subtracted number
        if currRes == target and len(num) == 0: # if result == target and all numbers have been used
            self.res.append(tmp)
            return
        # now divide into all situations
        for i in xrange(1, len(num)+1):
            currStr = num[:i]
            # remove the case of leading "0"
            if len(currStr) > 1 and currStr[0] == '0':
                return
            currNum = int(currStr)
            nextNum = num[i:] 
            if len(tmp) != 0: # do not insert operator for the first char
                self.helper(nextNum, target, tmp+'*'+currStr, currRes - prevNum + (currNum * prevNum), currNum * prevNum)
                self.helper(nextNum, target, tmp+'+'+currStr, currRes + currNum, currNum)
                self.helper(nextNum, target, tmp+'-'+currStr, currRes - currNum, - currNum)
            else:
                self.helper(nextNum, target, currStr, currNum, currNum)

s = Solution()
print s.addOperators('123',6)
            
                



 