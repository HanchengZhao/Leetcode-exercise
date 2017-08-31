class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {} # key is element, value is count
        res = []
        for i in nums1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for j in nums2:
            if j in dic and dic[j] > 0:
                res.append(j)
                dic[j] -= 1
        return res
'''
follow ups:

1. What if the given array is already sorted? How would you optimize your algorithm?

'''
# 2 pointers:
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res

'''
2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.

If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), then read 2 elements from each array at a time in memory, record intersections.
An improvement can be sort them using external sort, read (let's say) 2G of each into memory and then using the 2 pointer technique, then read 2G more from the array that has been exhausted. Repeat this until no more data to read from disk.

'''