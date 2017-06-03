class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        minSum,common = len(list1) + len(list2), []
        hashtable = dict()
        for i, rest in enumerate(list1):
            hashtable[rest] = i
        for i, rest in enumerate(list2):
            if rest in hashtable:
                if i + hashtable[rest] < minSum:
                    common = [rest]
                    minSum = i + hashtable[rest]
                elif i + hashtable[rest] == minSum:
                    common.append(rest)
        return common