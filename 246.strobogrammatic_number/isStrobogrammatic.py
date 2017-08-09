class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        rotated = []
        for char in num:
            if char in dic:
                rotated.append(dic[char])
            else:
                return False
        # print "".join(rotated[::-1])
        return num == "".join(rotated[::-1])
s = Solution()
print s.isStrobogrammatic("828")