import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if not dic.get(num):
                dic[num] = 1
            else:
                dic[num] += 1
        return heapq.nlargest(k, dic, key = dic.get)
if __name__ == '__main__':
    s = Solution()
    s.topKFrequent([1,1,1,1,1,3,3,3,3,4], 2)