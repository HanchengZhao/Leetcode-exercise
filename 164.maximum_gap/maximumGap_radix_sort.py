class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        num = self.radixSort(num)
        res = 0
        for i in range(1, len(num)):
            res = max(num[i] - num[i - 1], res)
        return res

    def radixSort(self, num):
        for i in range(31):
            onebucket = []
            zerobucket = []
            needle = 1 << i
            for j in range(len(num)):
                if num[j] & needle != 0:
                    onebucket.append(num[j])
                else:
                    zerobucket.append(num[j])
            num = []
            num += zerobucket
            num += onebucket
        return num
s = Solution()
print s.maximumGap([1,2,3,4,5,6,5,2,4,7,9])