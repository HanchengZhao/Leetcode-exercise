class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {0:-1}
        s = 0
        for i, val in enumerate(nums):
            s += val
            if k != 0:
                s = s % k
            if s in map:
                if i - map[s] > 1:
                    return True
            else:
                map[s] = i
        return False
'''
use a map to record previous mod and index. O(n)
'''

'''
O(n) solution
'''
def findmultiples(arr, k):
    if len(arr) == 0:
        return False
    if k == 0:
        return True
    sum1 = 0
    for i in xrange(len(arr)):
        sum1 += arr[i]
        s = sum1
        for j in xrange(0, i-1):
            s -= arr[j]
            if s % k == 0:
                return True
    return False
