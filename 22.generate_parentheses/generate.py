class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, left, right, n):
            if len(cur) == n * 2:
                res.append(cur)
                return
            if left < n:
                backtrack(cur + "(", left + 1, right, n)
            # here is the trick to avoid invalid parenthesis, only append
            # closing parenthesis when there's extra open parenthesis
            if right < left:
                backtrack(cur + ")", left, right + 1, n)
        backtrack("", 0, 0, n)
        return res
# time O(2 ^ n)
