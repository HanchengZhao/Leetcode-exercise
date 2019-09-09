import bisect


class Solution:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        arr2.sort()
        dp = {-1: 0}
        for i in arr1:
            temp = {}
            for key in dp.keys():
                # if don't take element from arr2
                if i > key:
                    temp[i] = min(temp.get(i, float("inf")), dp[key])
                # if we take an element from arr2 , and  key < val
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    temp[arr2[loc]] = min(
                        temp.get(arr2[loc], float("inf")), dp[key] + 1)
            dp = temp
        # in the end, if we still have candidate for last number
        if dp:
            return min(dp.values())
        return -1


s = Solution()
# print(s.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4]))
# print(s.makeArrayIncreasing([1, 5, 3, 6, 7], [4, 3, 1]))
# print(s.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3]))
# # should be 5
# print(s.makeArrayIncreasing([0, 11, 6, 1, 4, 3], [5, 4, 11, 10, 1, 0]))
print(s.makeArrayIncreasing([5, 16, 19, 2, 1, 12, 7, 14, 5, 16], [
      6, 17, 4, 3, 6, 13, 4, 3, 18, 17, 16, 7, 14, 1, 16]))
