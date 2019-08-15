class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        # sort on the start point
        new_list = sorted(intervals, key=lambda x: x[0])
        res = []
        start = new_list[0][0]
        end = new_list[0][1]
        for i in new_list[1:]:
            # has overlapping
            if i[0] <= end:
                end = max(i[1], end)
            else:
                res.append([start, end])
                # update start and end point
                start, end = i[0], i[1]
        res.append([start, end])
        return res
