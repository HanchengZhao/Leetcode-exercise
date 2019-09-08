'''
We can solve this problem using dp, we define the state as:
dp[i] = {possible_value: operation_count}, which inludes all the possible values we can pick from arr1 and arr2 for current i,
to calculate dp[i+1], we traverse each key in dp[i] then find the larger number in arr2 to take, then plus the count

type: dp, binary search
time: m * n * log(n), where m is length of arr1, n is length of arr2
'''
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
