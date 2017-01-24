class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2)/2] + nums2[len(nums2)/2 - 1]) / float(2)
            else:
                return nums2[len(nums2)/2]

        if not nums2:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1)/2] + nums1[len(nums1)/2 - 1]) / float(2)
            else:
                return nums1[len(nums1)/2]

        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        count = 0
        lastElement = 0
        if (len1 + len2) % 2 == 1: #odd
            while count < (len1 + len2) / 2:
                if nums1[i] <= nums2[j] and i < len1-1:
                    i += 1
                elif j < len2-1:
                    j += 1
                count += 1
            return float(min(nums1[i], nums2[j]))
        else: #even
            while count < (len1 + len2) / 2:
                lastElement = nums1[i] if nums1 <= nums2[j] else nums2[j]
                if nums1[i] <= nums2[j] and i < len1-1:
                    i += 1
                elif j < len2-1:
                    j += 1
                count += 1
            return (lastElement + min(nums1[i], nums2[j])) / float(2)

if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([],[2])
    print s.findMedianSortedArrays([1,2],[3,4])