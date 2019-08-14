class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = []
        accumulate = 0
        for i in nums:
            if i == 1:
                accumulate += 1
            else:
                #
                if accumulate != 0:
                    count.append(accumulate)
                    accumulate = 0
                else:
                    count.append(0)
        # handle the end accumulate
        count.append(accumulate)
        # need to start from the first
        m = count[0]
        for i, val in enumerate(count):
            if i != 0:
                m = max(m, val + count[i-1]+1)
        return m

# the idea is to split the array between 0s, then add the adjacent count to find the max
