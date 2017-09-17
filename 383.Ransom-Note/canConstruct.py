class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for c in magazine:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        for i in ransomNote:
            if i not in dic or dic[i] < 1:
                return False
            dic[i] -= 1
        return True