class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        lst = list(str(num))
        dic = {}
        for i, val in enumerate(lst):
            dic[val] = i # last occurance
        for i, val in enumerate(lst):
            for j in xrange(9, int(val), -1):
                index = dic.get(str(j), 0)
                if index > i:
                    lst[i], lst[index] = lst[index], lst[i]
                    return int(''.join(lst))
        return num