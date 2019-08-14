class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        rst = []
        if not num: # target could be 0
            return rst
        self.helper(rst, "", num, target, 0, 0, 0)
        return rst
    def helper(self, rst, path, num, target, pos, eval, multed):
        if pos == len(num): # reach the end
            if target == eval:
                rst.append(path)
            return
        for i in xrange(pos, len(num)):
            if i != pos and num[pos] == '0':
                break
            cur = int(num[pos: i+1])
            if pos == 0:
                self.helper(rst, path + str(cur), num, target, i+1, eval + cur, cur)
            else:
                self.helper(rst, path + "+" + str(cur), num, target, i+1, eval + cur, cur)
                self.helper(rst, path + "-" + str(cur), num, target, i+1, eval - cur, - cur)
                self.helper(rst, path + "*" + str(cur), num, target, i+1, eval - multed + multed * cur, multed * cur)
'''
1. use helper funtion to do the backtracking, and append new found to the res, not return any value
2. checking the leading 0 part, should not have multiple leading 0s
3. should save the number used for multiplication, since it changes the order
4. do not insert operator for the first char
'''