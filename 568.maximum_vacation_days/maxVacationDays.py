class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if not flights or not days:
            return 0
        weekslen = len(days[0])
        dp = [[0] * (weekslen + 1) for i in xrange(len(days))]
        for week in xrange(weekslen-1, -1, -1):
            for cur_city in xrange(len(days)):
                dp[cur_city][week] = days[cur_city][week] + dp[cur_city][week + 1]
                for dest_city in xrange(len(days)):
                    if flights[cur_city][dest_city] == 1:
                        dp[cur_city][week] = max(days[dest_city][week] + dp[dest_city][week + 1], dp[cur_city][week])
        return dp[0][0]