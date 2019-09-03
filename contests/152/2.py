class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        point = 0
        s = sum(calories[:k])
        if s > upper:
            point = 1
        elif s < lower:
            point = -1
        for i in range(k, len(calories)):
            s += calories[i] - calories[i-k]
            print(s)
            if s > upper:
                point += 1
            elif s < lower:
                point -= 1
        return point


s = Solution()
print(s.dietPlanPerformance([6, 13, 8, 7, 10, 1, 12, 11], 6, 5, 37))
