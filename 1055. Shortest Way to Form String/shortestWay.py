class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        i = 0
        while i < len(target):
            if target[i] not in source:
                return -1
            j = i
            for k in range(len(source)):
                if j < len(target) and source[k] == target[j]:
                    j += 1
            count += 1
            i = j
        return count


'''
use greedy to find longest match string in each target loop

Time O(len(source) * len(target))
'''
