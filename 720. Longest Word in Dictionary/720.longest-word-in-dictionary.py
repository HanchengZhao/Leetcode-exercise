#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = {}
        longest = ""
        for w in words:
            # start from the trie root everytime
            node = trie
            length = 0
            # to track whether letters before the last one are all in trie
            finished = True
            for pre in w[:-1]:
                if pre in node:
                    node = node[pre]
                    length += 1
                else:
                    finished = False
                    break
            if finished:
                # extend 1 node
                node[w[-1]] = {}
                length += 1
            if length > len(longest):
                longest = w
        return longest
