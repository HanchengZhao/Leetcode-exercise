# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        #init
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        #store and sort the starting and ending point
        left, right = [], []
        for i in intervals:
            left.append(i.start)
            right.append(i.end)
        left.append(newInterval.start)
        right.append(newInterval.end)
        left.sort()
        right.sort()

        res = []
        for j in xrange(len(left)-1):
            if left[j] < right[j] and left[j+1] > right[j]:
                    res.append([left[j],right[j]])
            elif j == len(left)-2:
                    res.append([left[j],right[j]])
            else:
                for k in xrange(j, len(left)-1):
                    if left[k] < right[k] and left[k+1] > right[k]:
                        res.append([left[j],right[k]])
                    elif k == len(left)-2:
                        res.append([left[j],right[k+1]])
        return res


# s = Solution()
# print s.insert([[1,5]],[2,3])