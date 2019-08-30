class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        shorter = nums1 if len(nums1) <= len(nums2) else nums2
        longer = nums2 if len(nums2) >= len(nums1) else nums1
        s = set()
        res = set()
        for i in longer:
            s.add(i)
        for j in shorter:
            if j in s:
                res.add(j)
        return list(res)
        
        # one line
        # return list(set(nums1) & set(nums2))