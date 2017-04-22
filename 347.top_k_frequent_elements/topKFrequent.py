class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            if freq.has_key(num):
                freq[num] += 1
            else:
                freq[num] = 1

        bucket = [0]*(len(nums)+1)
        for num, freq in freq.items():
            if (bucket[freq] == 0):
                bucket[freq] = []
            bucket[freq].append(num)

        result = []
        i = len(bucket) - 1
        while i > 0 and k > 0:
            if (bucket[i] != 0):
                result += bucket[i]
                k -= len(bucket[i])
            i -= 1
        return result

s = Solution()
print s.topKFrequent([1,1,1,2,2,3], 2)