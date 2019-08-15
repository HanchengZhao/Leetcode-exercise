'''
It requires us to solve it in O(log(m+n)), so we have to apply binary search here.
The basic idea is to get i elements from nums1, j elements from num2 so that i+j = k, while k = (m + n + 1) /2
i, j here should also make A[i-1] < B[j], B[j-1] < A[i], assuming that they exist.

The edge case could be that both sides of the median are in first half or second half.

'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # let length of nums2 be longer than nums1
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        half_len = (m + n + 1) // 2
        min_i, max_i = 0, m

        while min_i <= max_i:
            i = min_i + (max_i - min_i) // 2
            j = half_len - i
            # i is too small
            if i < m and nums2[j-1] > nums1[i]:
                min_i = i + 1
            # i is too big
            elif i > 0 and nums1[i-1] > nums2[j]:
                max_i = i - 1
            # we get the perfect i here
            else:
                # max of left
                if j == 0:
                    max_of_left = nums1[i-1]
                elif i == 0:
                    max_of_left = nums2[j-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2 == 1:  # odd
                    return max_of_left

                # min of right
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2
        return 0.0
