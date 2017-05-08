class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # moore voting algorithm
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        for i in nums:
            if i == cand1:
                count1 += 1
            elif i == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = i, 1
            elif count2 == 0:
                cand2, count2 = i, 1
            else:
                count1 -= 1
                count2 -= 1
        return [i for i in (cand1, cand2) if nums.count(i) > len(nums) / 3]