# https://leetcode.com/problems/corporate-flight-bookings/discuss/328871/C%2B%2BJava-with-picture-O(n)
# The idea is to mark the addition point and reduction point in the result array, then accumulate
# from the beginning to the end
# time: O(n), where n is the length of bookings
# space: O(n)


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for _ in range(n)]
        for i in bookings:
            start = i[0]
            end = i[1]
            res[start-1] += i[2]  # accumulate seats from here to the
            if end < n:
                res[end] -= i[2]  # no need to accumulate, remove seats from now on
        for i in range(1, n):
            res[i] += res[i-1]
        return res
