'''
Notice that only the words are sorted lexicographically, not the chars with the word.

1. Build the graph based on the list:
  - check 2 neighbor words, find the first diff char, and append to the dependency list.
  - record all the character appeared
2. Apply topological sort:
  - return false when detectingthe cycle
  - dfs and append the char
'''
from collections import defaultdict


class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        # build graph
        orders = defaultdict(set)
        # record all the chars
        chars = set(words[0])
        for i in range(len(words) - 1):
            chars = chars | set(words[i+1])
            prev, cur = words[i], words[i+1]
            for j in range(min(len(prev), len(cur))):
                chars.add(prev[j])
                chars.add(cur[j])
                if prev[j] != cur[j]:
                    orders[cur[j]].add(prev[j])
                    break
        res = []
        visited = set()
        visiting = set()

        def dfs(char, visited, visiting, orders):
            if char in visited:
                return True
            if char in visiting:
                return False
            visiting.add(char)
            for dep in orders[char]:
                if not dfs(dep, visited, visiting, orders):
                    return False
            res.append(char)
            visited.add(char)
            visiting.remove(char)
            return True
        for char in chars:
            if not dfs(char, visited, visiting, orders):
                return ""
        return "".join(res)


s = Solution()
print(s.alienOrder(["ab", "adc"]))
