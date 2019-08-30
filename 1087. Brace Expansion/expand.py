class Solution:
    def expand(self, S: str) -> List[str]:
        res = []

        def backtrack(s, word):
            if not s:
                res.append(word)
            else:
                if s[0] == "{":
                    i = s.index("}")
                    for w in s[1:i].split(","):
                        backtrack(s[i+1:], word + w)
                else:
                    backtrack(s[1:], word + s[0])
        backtrack(S, "")
        res.sort()
        return res
