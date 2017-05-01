class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        digit = ""
        while i < len(word) and j < len(abbr):
            #count digit
            if abbr[j].isdigit():
                if not digit and abbr[j] == "0": # avoid leading 0
                    return False
                digit += abbr[j]
                j += 1
            elif digit:
                i += int(digit)
                digit = ""
            elif word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False
        if digit: i += int(digit)  # handle the digit at the end
        if i == len(word) and j == len(abbr):
            return True
        else:
            return False
s = Solution()
print s.validWordAbbreviation("internationalization", "i012iz4n")