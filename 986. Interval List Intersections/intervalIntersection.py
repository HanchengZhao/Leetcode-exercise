class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []

        def getOverlap(a, b):
            if a[1] < b[0] or b[1] < a[0]:
                return []
            left = max(a[0], b[0])
            right = min(a[1], b[1])
            return [left, right]
        i, j = 0, 0
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            overlap = getOverlap(a, b)
            if overlap:
                res.append(overlap)
            if a[1] <= b[1]:
                i += 1
            else:
                j += 1
        return res


'''
use 2 pointers to move forward
time: O(M + N)
'''
