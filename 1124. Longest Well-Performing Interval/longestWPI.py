class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # the question will be turned into find the max length of subarray
        # that has positive sum
        converts = [1 if i > 8 else -1 for i in hours]

        longest = 0
        # save first appearance sum : index
        # only need to record negative sums, cause for every positive sum,
        # we can set the current longest length to it
        prefix = {0: -1}
        s = 0
        for i, val in enumerate(converts):
            s += val
            if s > 0:
                longest = i + 1
            else:
                if s not in prefix:
                    prefix[s] = i
                # because the gap between consecutive sum is always 1
                # we will get the longest interval just by find the sum that's
                # 1 smaller than the current one, and let s - (s-1), which is positive
                longest = max(longest, i - prefix.get(s - 1, i))
        return longest
# time: O(n)
