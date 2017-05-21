from fractions import Fraction
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        res = Fraction(0)
        end = len(expression)
        for i in xrange(len(expression)-1, -1, -1):
            if expression[i] == "-":
                res -= Fraction(expression[i+1:end])
                end = i
            if expression[i] == "+":
                res += Fraction(expression[i+1:end])
                end = i
        if expression[0] != "-":
            res += Fraction(expression[:end])
        return str(res.numerator) + "/" + str(res.denominator)

# using fractions library is somewhat cheating, try do it using gcd or lcm

s = Solution()
print s.fractionAddition("-1/2+1/2")
print s.fractionAddition("5/3+1/3")
