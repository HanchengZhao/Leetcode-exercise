class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = mintemp = maxtemp = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                # swap min and max temp if integer is negative
                mintemp, maxtemp = maxtemp, mintemp

            # either restart from this number or let this num multiply previous maximum
            maxtemp = max(nums[i], nums[i] * maxtemp)
            mintemp = min(nums[i], nums[i] * mintemp)
            maximum = max(maximum, maxtemp)
        return maximum


'''
so the idea is to keep track of the max and min product up to this number:
for every number, consider either restarting from this one or multiply the previous max/min
O(n) time, O(1) space
'''

'''
what if asking to return the interval of maximum product, like (0,1)
'''


class Solution2(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = mintemp = maxtemp = nums[0]
        start = {min: 0, max: 0}
        interval = (0, 0)
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                # swap min and max temp if integer is negative
                mintemp, maxtemp = maxtemp, mintemp
                startIndex = start[min]
            else:
                startIndex = start[max]
            if nums[i] > nums[i] * maxtemp:  # restart from this number
                maxtemp = nums[i]
                start[max] = i
                if maxtemp > maximum:
                    interval = (i, i)
                    maximum = maxtemp
            else:
                maxtemp = nums[i] * maxtemp
                if maxtemp > maximum:
                    interval = (startIndex, i)
                    maximum = maxtemp
            if nums[i] < nums[i] * mintemp:
                mintemp = nums[i]
                start[min] = i
            else:
                mintemp = nums[i] * mintemp

        return interval


s = Solution2()
print s.maxProduct([2, 3, -2, 4, 4, -7])
