'''
We can use a binary search to solve it. The value is the target sum we want to get

The left bound would be max(nums), where every number is in a group
The right bound is Sum(nums), where m = 1

for each candidate, we traverse the array to get prefix sum, and tracking the count of groups
we get so far, if the count < m, which means, candidate can be smaller and vice versa
then we can solve the problem in O(log(sum(nums)) * n)
'''


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        n = len(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            # temporary sum in this group
            s = 0
            # group count
            count = 0
            for i in range(n):
                # too big, move to next group
                if s + nums[i] > mid:
                    s = nums[i]
                    count += 1
                else:
                    s += nums[i]
            if count < m:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
