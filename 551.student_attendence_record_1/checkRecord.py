class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        late_count = 0
        absent_count = 0
        for i in s:
            if i == "A":
                absent_count += 1
                if absent_count > 1:
                    return False
            if i == "L":
                late_count += 1
                if late_count > 2:
                    return False
            else: late_count = 0
        return True