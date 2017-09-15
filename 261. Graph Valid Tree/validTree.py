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
            if nums[i] == i: # is its own root
                return i
            return find(nums, nums[i])
        nums = range(n)
        for e in edges:
            x = find(nums, e[0])
            y = find(nums, e[1])
            if x == y: # there is a cycle
                return False
            nums[x] = y # set the parent
        # in the end, if there is no cycle and there n-1 edges, all node will be connected
        return len(edges) == n-1 
        

    
