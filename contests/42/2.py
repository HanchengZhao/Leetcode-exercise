class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # newpairs = sorted(pairs, key=lambda x: x[0])
        # print newpairs
        hashmap = {}
        for i in pairs:
            if i[0] not in hashmap:
                hashmap[i[0]] = i[1]
            else:
                hashmap[i[0]] = min(hashmap[i[0]], i[1])
        count = 0
        keys = sorted(hashmap.keys())
        lastend = float('-inf')
        # laststart = keys[0]
        #print hashmap, keys
        for key in keys:
            if key > lastend:
                count += 1
                lastend = hashmap[key]
            else:
                lastend = min(hashmap[key],lastend)
        return count

s = Solution()
print s.findLongestChain([[1,2], [2,3], [3,4],[1,1],[5,6]])
print s.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]) # 3