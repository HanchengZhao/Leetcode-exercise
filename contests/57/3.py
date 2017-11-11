class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        # block: check for opening and ending
        # line: check for //
        res = []
        blockopen = False
        for line in source:
            content = ""
            if blockopen:
                if '*/' in line:
                    index = line.index('*/')
                    content = line[index+2:]
                    blockopen = False
            else:
                if '/*' in line:
                    blockindex = line.index('/*')
                    if '//' in line:
                        lineindex = line.index('//')
                        if lineindex < blockindex:
                            content = line[:lineindex]
                        else:
                            content = line[:blockindex]
                            blockopen = True
                    elif '*/' in line:
                        index = line.index('*/')
                        content = line[index+2:]
                        blockopen = False
                    else:
                        content = line[:blockindex]
                        blockopen = True
                elif '//' in line:
                    lineindex = line.index('//')
                    content = line[:lineindex]
                else:
                    content = line
            if len(content) != 0:
                res.append(content)
        return res
s = Solution()
print s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
print s.removeComments(["a/*comment", "line", "more_comment*/b"])#"ab"