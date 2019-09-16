#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        waitings = defaultdict(list)
        for w in words:
            waitings[w[0]].append(w[1:])
        for i in S:
            suffix = waitings[i]
            waitings[i] = []
            for w in suffix:
                if not w:
                    count += 1
                else:
                    waitings[w[0]].append(w[1:])
        return count


'''
We can only loop each char in S once, then loop through the words to see
if the first char of each word matches, then continue.

time: O(s + ∑words[i].length), s is the length of S
'''
