class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # cur contains all the words in one row, but can also be used for counting needed spaces
        res, cur, num_of_letters = [], [], 0 
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth: # get enough words in one row
                for i in xrange(maxWidth - num_of_letters):
                    cur[i % (len(cur)-1 or 1)] += ' ' # round robin, use mod to choose the position to add space
                res.append(''.join(cur)) # finish inserting spaces
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)] # the last cur
s = Solution()
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."," ff"], 16)
# https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines