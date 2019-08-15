class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        # dp[i] indicates the maximum fuel we get after stopping for i steps
        dp = [0] * (n + 1)
        dp[0] = startFuel
        for i in range(n):
            for j in range(i, -1, -1):
                # if you can reach the station i with enough fuel
                # check if we can update the maximum fuel by stopping here
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
        for i, val in enumerate(dp):
            # get the minimum steps to exceed the target length
            if val >= target:
                return i
        return -1

# time: O(n^2), space: O(n)
# The difficult part here is to find the way to define the dp state
# and update state accordingly.
