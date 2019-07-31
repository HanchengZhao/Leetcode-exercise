class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        cache = {}
        # start from position i

        def dfs(i, M):
            if (i, M) in cache:
                return cache[i, M]
            if i + 2 * M >= n:
                return sum(piles[i:])
            Max = 0
            for X in range(1, 2 * M + 1):
                # use the rest sum to subtract the rest max
                Max = max(Max, sum(piles[i:]) - dfs(i + X, max(M, X)))
            cache[(i, M)] = Max
            return cache[(i, M)]
        return dfs(0, 1)
