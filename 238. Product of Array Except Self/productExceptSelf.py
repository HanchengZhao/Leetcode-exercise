class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # since we can not use division, we need to record the privous product
        # we can sweep the array from the beginning and the end, and get 
        # the product below this index and above this index
        output = []
        p = 1
        for i in xrange(len(nums)):
            output.append(p) # save the product below the index
            p *= nums[i] # get product
        p = 1
        for i in xrange(len(nums)-1, -1, -1):
            output[i] *= p # multiply the product above the index
            p *= nums[i]
        return output
        