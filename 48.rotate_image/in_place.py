'''
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''


class Solution:
    def rotate(self, A):
        n = len(A)
        A.reverse()
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
