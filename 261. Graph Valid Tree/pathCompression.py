class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # should have no cycles
        # should have no independent pairs
        def find(nums, i):
            while nums[i] != i: # do the compression in the process
                nums[i] = nums[nums[i]]
                i = nums[i]
            return i
        nums = range(n)
        for e in edges:
            x = find(nums, e[0])
            y = find(nums, e[1])
            if x == y: # there is a cycle
                return False
            nums[x] = y
        return len(edges) == n-1
# time: 42ms