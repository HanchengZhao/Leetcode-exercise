class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num: # target could be 0
            return []
        res = []
        self.helper(res, num, target, '', 0, 0)
        return res
        
    def helper(self,res, num, target, path, curval, multi):
        if len(num) == 0 and curval == target:
            res.append(path)
            return
        for i in xrange(1, len(num)+1): #i could reach len(num)
            curStr = num[:i]
            curNum = int(curStr)
            if len(curStr) > 1 and curStr[0] == '0':
                return
            nextStr = num[i:]
            if len(path) == 0: # do not insert operators in the front
                self.helper(res, nextStr, target, curStr, curNum, curNum)
            else:
                self.helper(res, nextStr, target, path + '+' + curStr, curval + curNum, curNum)
                self.helper(res, nextStr, target, path + '-' + curStr, curval - curNum, -curNum)
                self.helper(res, nextStr, target, path + '*' + curStr, curval - multi + curNum * multi, multi* curNum)
'''
1. use helper funtion to do the backtracking, and append new found to the res, not return any value
2. checking the leading 0 part, should not have multiple leading 0s
3. should save the number used for multiplication, since it changes the order
4. do not insert operator for the first char
'''