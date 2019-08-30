class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        def handleRange(l, r, res):
            if r - l <= 1:
                return
            if r - l == 2:
                res.append(str(r-1))
            else:
                res.append("{}->{}".format(l+1, r-1))
        if not nums:
            handleRange(lower-1, upper+1, res)
            return res
        handleRange(lower-1, nums[0], res)
        for i in range(1, len(nums)):
            handleRange(nums[i-1], nums[i], res)
        handleRange(nums[-1], upper+1, res)
        return res