class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        j = 0
        while j < len(A) and A[j] < 0:
            j += 1
        i = j-1
        while i >= 0 and j < len(A):
            if A[i] ** 2 < A[j] ** 2:
                res.append(A[i] ** 2)
                i -= 1
            else:
                res.append(A[j] ** 2)
                j += 1
        while i >= 0:
            res.append(A[i] ** 2)
            i -= 1
        while j < len(A):
            res.append(A[j] ** 2)
            j += 1
        return res


'''
O(n)
one pass, use 2 pointers to loop through all the positive numbers and negative numbers
append smaller square number to the result
'''
