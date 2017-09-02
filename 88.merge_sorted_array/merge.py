class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        # start from the end and put the larger number first
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]: 
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k -= 1
        if n > 0: # if nums in nums1 have been used and nums2 has numbers left
            nums1[:n] = nums2[:n]