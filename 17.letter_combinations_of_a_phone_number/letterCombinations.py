class Solution(object):
    def cartesion(self, x, y):
        # print "x: " + str(x) , "y: " + str(y)
        combined = []
        for i in x:
            for j in y:
                combined.append(i+j)
        return combined

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict=[[''],['_'],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        result = []
        if(digits):
            result = reduce(self.cartesion, map(lambda x:dict[int(x)], digits))
        return result
s = Solution()
print s.letterCombinations("1234")
