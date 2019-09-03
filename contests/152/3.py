from collections import Counter
import copy


class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        res = []
        memo = [{} for _ in range(len(s) + 1)]
        c = Counter()
        for i in range(len(s)):
            c.update(s[i])
            memo[i+1] = copy.copy(c)

        def palindromeMiss(c):
            odd = -1
            print(c)
            for v in c.values():
                if v > 0 and v % 2 == 1:
                    odd += 1
            return max(0, odd)

        for query in queries:
            left, right, k = query
            c = copy.copy(memo[right])
            c.subtract(memo[left-1])
            if palindromeMiss(c) <= 2 * k:
                res.append(True)
            else:
                res.append(False)
        return res


s = Solution()
print(s.canMakePaliQueries("abcda", [[3, 3, 0], [
      1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))

# print(s.canMakePaliQueries("hunu",
#                            [[1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 2], [1, 3, 3], [2, 3, 1], [3, 3, 1], [0, 3, 0], [1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 1], [1, 1, 1]]))
