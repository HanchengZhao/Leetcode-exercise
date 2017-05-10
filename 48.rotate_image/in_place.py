class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])