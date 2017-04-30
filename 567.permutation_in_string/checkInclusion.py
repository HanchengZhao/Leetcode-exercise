class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a = [(ord(c) - ord("a")) for c in s1 ]
        b = [(ord(c) - ord("a")) for c in s2 ]

        target = [0] * 26
        for i in a:
            target[i] += 1
        #sliding window
        window = [0] * 26
        for i in xrange(len(b)):
            window[b[i]] += 1
            if i > len(a):
                window[b[i-len(a)]] -= 1
            if window == target:
                return True
        return False
