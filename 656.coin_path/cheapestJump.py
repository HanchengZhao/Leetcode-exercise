class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        dp = [0 for i in xrange(len(A))]
        path = {}
        for i in xrange(len(A)):
            if A[i] == -1:
                dp[i] = float('inf')
                path[i] = []
                continue
            start = i-B if i-B >=0 else 0
            prev = dp[start:i]
            if prev:
                minimum = min(prev)
                #index = i - len(prev) + prev.index(minimum)  this will only find the first occurance, but it needs last occurance here
                for j in xrange(len(prev)-1, -1, -1):
                    if prev[j] == minimum:
                        index = i - len(prev) + j
                        break
                dp[i] = minimum + A[i]
                path[i] = path[index] + [i+1]
            else: # for the first
                dp[i] = A[i]
                path[i] = [i+1]

        if dp[-1] == float('inf'):
            return []
        else:
            return path[len(A) - 1]
# error        
solution = Solution()
print solution.cheapestJump([1,2,4,-1,2], 2)
print solution.cheapestJump([1,2,4,-1,2], 1)
print solution.cheapestJump([0,0,0,0,0,0], 3) # in this case, it will find the first occurance