class Solution:
    def minIncrementForUnique(self, A):
        A.sort()
        count = 0
        for i, val in enumerate(A):
            if i > 0 and val <= A[i-1]:
                count += A[i-1] - val + 1
                A[i] = A[i-1] + 1
        return count
