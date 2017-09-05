class Solution(object):
    def __init__(self):
        self.memo = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
    def letterCombinations(self, digits):
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, "", res)
        return res
    
    def dfs(self, digits, idx, path, res):
        if len(path) == len(digits):
            res.append(path)
            return  # backtrack
        for i in range(idx,len(digits)):
            for c in self.memo[digits[i]]:
                self.dfs(digits, i+1, path+c, res)