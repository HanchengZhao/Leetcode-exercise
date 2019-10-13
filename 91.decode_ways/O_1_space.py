class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        last_one, last_two = 1, 1
        for i in range(1, len(s)):
            # invalid
            if s[i] == "0" and (s[i-1] != "1" and s[i-1] != "2"):
                return 0
            if s[i] == "0":
                temp = last_two
            elif s[i-1] == "1" or s[i-1] == "2" and 0 <= int(s[i]) <= 6:
                temp = last_one + last_two
            else:
                temp = last_one
            last_two = last_one
            last_one = temp
        return last_one
        