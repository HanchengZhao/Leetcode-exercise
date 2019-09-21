class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        # smallest is the bound for us to choose dividends in next level

        def divide(num, smallest, prev, res):
            # the right bound should be sqrt(num) instead of num / 2, because we
            # want the first factor to be smaller than second
            for i in range(smallest, int(num ** 0.5) + 1):
                if num % i == 0 and (num // i) >= max(smallest, i):
                    divide(num//i, i, prev + [i], res)
            if len(prev) > 0:
                res.append(prev + [num])
        divide(n, 2, [], res)
        return res


'''
When we go to next level, factors we generate shouldn't be smaller than the 
factors we use before in prev.

say, n = 12
12
  - 2 , 6
        - 2, 3
  - 3, 4
       (2, 2) won't use this because 3 is the smallest when we get into this level

in the end, the res would be sorted and contain no duplicates
'''
