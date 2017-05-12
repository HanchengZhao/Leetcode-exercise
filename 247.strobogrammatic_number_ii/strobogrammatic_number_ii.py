'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
'''

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        self.res = []
        self.recursion(n, "", "")
        return self.res

    def recursion(self, n, str1, str2):
        if n == 0:
            self.res.append(str1 + str2)
            return
        if n == 1:
            self.res.append(str1 + "0" + str2)
            self.res.append(str1 + "1" + str2)
            self.res.append(str1 + "8" + str2)
        else:
            if str1 and str1[0] != "0": # 0 can not be at the beginning
                self.recursion(n-2, str1 + "0", "0" + str2)
            self.recursion(n-2, str1 + "6", "9" + str2)
            self.recursion(n-2, str1 + "8", "8" + str2)
            self.recursion(n-2, str1 + "1", "1" + str2)
            self.recursion(n-2, str1 + "9", "6" + str2)

s = Solution()
print s.findStrobogrammatic(2)