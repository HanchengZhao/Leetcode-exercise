from collections import defaultdict


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        row = defaultdict(int)
        col = defaultdict(int)
        diag = defaultdict(int)
        antd = defaultdict(int)
        Max = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if not M[i][j]:
                    row[i] = col[j] = antd[i+j] = diag[i-j] = 0
                else:
                    row[i] += 1
                    col[j] += 1
                    antd[i+j] += 1
                    diag[i-j] += 1
                    Max = max(Max, row[i], col[j], antd[i+j], diag[i-j])
        return Max
