class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        longest = ""
        for i in d:
            spointer = 0
            dpointer = 0
            while dpointer < len(i) and spointer < len(s):
                if s[spointer] == i[dpointer]:
                    spointer += 1
                    dpointer += 1
                else:
                    spointer += 1
            if dpointer == len(i) and len(i) > len(longest): #match
                longest = i
        return longest
s = Solution()
print s.findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
print s.findLongestWord("abpcplea", ["a","b","c"])