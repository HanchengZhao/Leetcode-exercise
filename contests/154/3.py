class Solution:
    def kConcatenationMaxSum(self, arr, k) -> int:
        modulo = 10 ** 9 + 7

        def findMaxSum(arr):
            Max = 0
            cur = 0
            for i in arr:
                cur = max(cur + i, 0)
                Max = max(Max, cur)
            return Max

        def findleftMax(arr):
            Max = 0
            cur = 0
            for i in arr:
                cur += i
                Max = max(Max, cur)
            return Max

        def findrightMax(arr):
            Max = 0
            cur = 0
            for i in range(len(arr)-1, -1, -1):
                cur += arr[i]
                Max = max(Max, cur)
            return Max

        s = sum(arr)
        # print(s, findleftMax(arr), findrightMax(arr))
        if s > 0:
            if k < 3:
                return max(s * k, findleftMax(arr) + findrightMax(arr)) % modulo
            else:
                return max(s * k, findleftMax(arr) + s * (k-2) + findrightMax(arr)) % modulo
        else:
            return max(findleftMax(arr) + findrightMax(arr), findMaxSum(arr))


s = Solution()
print(s.kConcatenationMaxSum([1, 2], 3))
print(s.kConcatenationMaxSum([1, -2, 1], 5))
print(s.kConcatenationMaxSum([-1, -2], 7))
print(s.kConcatenationMaxSum([-5, 4, -4, -3, 5, -3], 3))
print(s.kConcatenationMaxSum([-5, -2, 0, 0, 3, 9, -2, -5, 4], 5))
print(s.kConcatenationMaxSum(
    [-9, 13, 4, -16, -12, -16, 3, -7, 5, -16, 16, 8, -1, -13, 15, 3], 6))
# print(s.kConcatenationMaxSum([1, 2], 3))
