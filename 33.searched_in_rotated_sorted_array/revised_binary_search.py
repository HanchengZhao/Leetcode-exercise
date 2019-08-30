class Solution(object):
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(arr) == 0:
            return -1
        lo, hi = 0, len(arr)-1
        while lo < hi:
            mid = (lo + hi) / 2
            if arr[mid] == target:
                return mid
            if arr[lo] <= arr[mid]: # if the left is sorted
                if arr[lo] <= target and target < arr[mid]: # in the left, target could equal to arr[lo]
                    hi = mid - 1
                else: # in the right
                    lo = mid + 1
            else: # the right is sorted
                if arr[mid] < target and target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return lo if arr[lo] == target else -1 # lo == right
'''
compare the mid value, if not found, check if the left subarray is sorted 
if sorted, check whether the target is in this interval by comparing the target with
lo and hi part, do the same thing for right part

'''