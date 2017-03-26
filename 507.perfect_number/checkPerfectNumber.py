class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        sum = 0
        divisors = set(reduce(list.__add__,
                ([i, num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0)))
        for i in divisors:
            sum += i
        return sum == 2*num