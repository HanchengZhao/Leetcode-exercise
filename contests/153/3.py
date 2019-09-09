class Solution:
    def maximumSum(self, arr) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        no_deletion = arr[:]
        for i in range(1, n):
            no_deletion[i] = max(no_deletion[i-1], 0) + arr[i]
        with_deletion = arr[:]
        Max = arr[0]
        for i in range(1, n):
            with_deletion[i] = max(
                with_deletion[i-1], no_deletion[i-2] if i > 1 else 0, 0) + arr[i]
            Max = max(Max, with_deletion[i])
        return Max


s = Solution()

print(s.maximumSum([1, -2, 0, 3]))
print(s.maximumSum([1, -2, -2, 3]))
# 17
print(s.maximumSum([8, -1, 6, -7, -4, 5, -4, 7, -6]))
