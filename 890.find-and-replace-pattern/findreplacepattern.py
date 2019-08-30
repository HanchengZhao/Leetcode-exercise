#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def findIso(a, b):
            if len(a) != len(b):
                return False
            m1 = {}
            m2 = {}
            for i in range(len(a)):
                if a[i] not in m1 and b[i] not in m2:
                    m1[a[i]] = b[i]
                    m2[b[i]] = a[i]
                else:
                    v1 = m1.get(a[i], 1)
                    v2 = m2.get(b[i], 2)
                    if v1 != b[i] or v2 != a[i]:
                        return False
            return True
        return [w for w in words if findIso(w, pattern)]
