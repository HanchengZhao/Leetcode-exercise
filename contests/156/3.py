class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            ns = s[0]
            dupcount = 1
            removed = False
            for i in range(1, len(s)):
                ns += s[i]
                if s[i] == s[i-1] and not removed:
                    dupcount += 1
                    if dupcount == k:
                        ns = ns[:-dupcount]
                        removed = True
                        dupcount = 1
                else:
                    dupcount = 1
                    removed = False
            if ns == s:
                break
            s = ns
        return s
s = Solution()
print(s.removeDuplicates("abcd", 2))
print(s.removeDuplicates("deeedbbcccbdaa", 3))
print(s.removeDuplicates("pbbcggttciiippooaais", 2))