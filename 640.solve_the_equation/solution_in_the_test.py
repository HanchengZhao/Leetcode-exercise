class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left = equation.split("=")[0]
        right = equation.split("=")[1]
        sign = 1 # used to check positive or negative
        xleft = 0
        leftsum = 0 #digit sum
        xright = 0
        rightsum = 0
        lastsign = 0
        for i in xrange(len(left)):
            if left[i] == "+" or left[i] == "-":
                if i == 0:
                    sign = 1 if left[i] == "+" else -1
                    lastsign = i + 1
                    continue
                part = left[lastsign:i]
                if "x" in part:
                    if len(part) == 1:
                        xleft += sign
                    else:
                        xleft += sign * int(part[:-1])
                else:
                    leftsum += sign * int(part)
                sign = 1
                lastsign = i + 1
                sign = 1 if left[i] == "+" else -1
        lastpart = left[lastsign:]
        if "x" in lastpart:
            if len(lastpart) == 1:
                xleft += sign
            else:
                xleft += sign * int(lastpart[:-1])
        else:
            leftsum += sign * int(lastpart)
        sign = 1
        lastsign = 0
        for i in xrange(len(right)):
            if right[i] == "+" or right[i] == "-":
                if i == 0:
                    sign = 1 if left[i] == "+" else -1
                    lastsign = i + 1
                    continue
                part = right[lastsign:i]
                if "x" in part:
                    if len(part) == 1:
                        xright += sign
                    else:
                        xright += sign * int(part[:-1])
                else:
                    rightsum += sign * int(part)
                sign = 1
                lastsign = i + 1
                sign = 1 if right[i] == "+" else -1
        lastpart = right[lastsign:]
        if "x" in lastpart:
            if len(lastpart) == 1:
                xright += sign
            else:
                xright += sign * int(lastpart[:-1])
        else:
            rightsum += sign * int(lastpart)
        if xleft == xright:
            if leftsum == rightsum:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            res = (rightsum - leftsum) / (xleft - xright)
            return "x=" + str(res)
# it was so hard to come up with an elegant solution while in the middle of the contest
# so my idea was to separate equation into left and right part and count the x and digit sum
# then do the math