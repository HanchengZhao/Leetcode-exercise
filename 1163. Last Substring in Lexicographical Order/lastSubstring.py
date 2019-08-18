'''
Start from the end, check each char, if it's larger than
saved char, 
1. if smaller, move forward,
2, if its larger:
    save the current char as the largest
3, if the same:
    compare the substring
'''


class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        last = s[-1]
        maxchar = last
        for i in range(n-2, -1, -1):
            if s[i] < maxchar:
                continue
            if s[i] > maxchar:
                maxchar = s[i]
                last = s[i:]
            else:
                last = max(last, s[i:])
        return last
