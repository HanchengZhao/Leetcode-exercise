class Solution(object):
    def letterCombinations(self, digits):
        mapping=[[''],['_'],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        res = ['']
        for i in digits:
            strings = mapping[int(i)]
            res = [i+j for j in strings for i in res]
        return res
s = Solution()
print s.letterCombinations('23')