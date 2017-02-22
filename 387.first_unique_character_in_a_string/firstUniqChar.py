class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = []
        unique = []
        for i in s:
            if i not in used:
                used.append(i)
                unique.append(i)
            else:
                if i in unique:
                    unique.remove(i)
        if not unique:
            return -1
        else:
            return s.index(unique[0])