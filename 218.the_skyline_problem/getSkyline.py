import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        xs = []
        # append all x coordinates
        for l, r, h in buildings:
            xs.append(l)
            xs.append(r)
        xs.sort()
        result, activeheap, i = [], [], 0
        for x in xs:
            #if the rect.end < x, the rect has been checked, romove the rect
            while activeheap and activeheap[0][1] <= x:
                heapq.heappop(activeheap)
            # starting building based on x
            while i < len(buildings) and buildings[i][0]==x:
                #in order to maintain max-heap, height is changed to negative
                heapq.heappush(activeheap, (-buildings[i][2], buildings[i][1]))
                i += 1
            #y is either 0 or max height
            y = 0 if not activeheap else -activeheap[0][0]
            #if y changes
            if not result or result[-1][1] != y: # if there is no previous building or change
                result.append([x, y])
        return result
'''
so the basic idea is:
step 1: push all the start and end point to the array and sort
step 2: loop through the array:
    1.if meet the start point, push (height, end point) to the heap, # putting height in the front to sort
    2.if meet the end point, check if it is already behind, otherwise
    3.check the max height everytime, add to the result only if y changes
'''
