# it requires us to do it in place, so we can't use extra space here
# we can do it in 2 passes, the first pass record the count of 0s as shifts
# the second pass put the shifted elements in the right spot and put 0s in the right spot
# e.g, [1,0,2,3,0,4,5,0] will be extended as [1,0,0,2,3,0,0,4],5,0,0, only the first 8 elememnts
# fit in the array
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        shift = 0
        l = len(arr)
        for i in range(l):
            if arr[i] == 0:
                shift += 1
        for i in range(l-1, -1, -1):
            # put the shifted number in the right spot
            if i + shift < l:
                arr[i+shift] = arr[i]
            # if we meet a 0, we need to duplicate 0
            if arr[i] == 0:
                shift -= 1
                if i + shift < l:
                    arr[i+shift] = 0
