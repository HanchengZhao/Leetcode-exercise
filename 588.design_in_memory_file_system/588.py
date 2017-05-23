from collections import defaultdict
class FileSystem(object):

    def __init__(self):
        self.folder = defaultdict(set)
        self.file = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        return sorted((self.folder.get(path,[]))) # in lexicographic order

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        # get each folder
        folder = path.split("/")
        for i in xrange(len(folder)-1):
            if folder[i]:
                self.folder["/".join(folder[:i+1])].add(str(folder[i+1]))
            else:# ""
                self.folder["/"].add(str(folder[i+1]))

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        #append to file content
        self.file[filePath] = self.file.get(filePath,"") + content
        folder = filePath.split("/")
        self.folder[filePath].add(folder[-1])
        for i in xrange(len(folder)-1):
            if folder[i]:
                self.folder["/".join(folder[:i+1])].add(str(folder[i+1]))
            else:
                self.folder["/"].add(str(folder[i+1]))

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.file[filePath]



# Your FileSystem object will be instantiated and called as such:
# if __name__ == '__main__':
#     path1 = "/"
#     path2 = "/a/b/c"
#     filePath = "/a/b/c/d"
#     content = "hello"
#     content2 = "world"

#     obj = FileSystem()
#     param_1 = obj.ls(path1)
#     obj.mkdir(path2)
#     obj.addContentToFile(filePath,content)
#     obj.addContentToFile(filePath,content2)
#     print obj.ls(filePath)
#     param_4 = obj.readContentFromFile(filePath)
#     param_5 = obj.ls(path1)
#     print param_1, param_4, param_5
#     print obj.folder