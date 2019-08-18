class Solution:
    def lastSubstring(self, s: str) -> str:
        index = 0
        uni = 0
        for i, val in enumerate(s):
            if ord(val) > uni:
                uni = ord(val)
                index = i
        return s[index:]


s = Solution()
print(s.lastSubstring("abab"))
print(s.lastSubstring("leetcode"))
print(s.lastSubstring(
    "xbylisvborylklftlkcioajuxwdhahdgezvyjbgaznzayfwsaumeccpfwamfzmkinezzwobllyxktqeibfoupcpptncggrdqbkji"))
