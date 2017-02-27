class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(x) for x in nums]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'

s = Solution()
print s.largestNumber([3, 30, 34, 5, 9])