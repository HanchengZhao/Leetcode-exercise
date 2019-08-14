class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            mi = min(arr)
            i = arr.index(mi)
            left = arr[i-1] if i > 0 else float("inf")
            right = arr[i+1] if i < len(arr)-1 else float("inf")
            if left < right:
                res += left * mi
            else:
                res += right * mi
            arr.pop(i)
        return res
