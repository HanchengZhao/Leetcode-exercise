class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip("\t")
            depth = len(line) - len(name)
            if "." in name: #if it is a file
                maxlen = max(pathlen[depth]+len(name), maxlen)
            else:
                pathlen[depth+1] = len(name) + pathlen[depth]+1
        return maxlen