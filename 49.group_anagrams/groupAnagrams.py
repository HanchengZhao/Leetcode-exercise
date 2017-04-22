class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[]]
        dic = dict()
        for i in strs:
            comb = "".join(sorted(i))
            if dic.get(comb):
                dic[comb].append(i)
            else:
                dic[comb] = [i]
        return dic.values()