import datetime
import calendar


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = datetime.datetime(year, month, day).weekday()
        return (calendar.day_name[date])


s = Solution()
print(s.dayOfTheWeek(31, 8, 2019))
