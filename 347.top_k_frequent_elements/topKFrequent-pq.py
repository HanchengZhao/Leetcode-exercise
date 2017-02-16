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
        print heapq.nlargest(k, dic, key = dic.get)
        print dic
if __name__ == '__main__':
    s = Solution()
    s.topKFrequent([1,1,1,1,1,3,3,3,3,4], 2)