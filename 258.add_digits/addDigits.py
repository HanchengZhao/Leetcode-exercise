class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        nxt = 0
        while num:
            nxt += (num % 10)
            num = num / 10
        return self.addDigits(nxt)

#one liner

class Solution1(object):
    def addDigits(self, num):
        return (num % 9 or 9) if num else 0