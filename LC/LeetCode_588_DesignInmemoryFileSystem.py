import collections
import bisect

class FileSystem(object):

    def __init__(self):
        self.paths = collections.defaultdict(list)
        self.files = collections.defaultdict(str)

    def ls(self, path):
        if path in self.files:
          return [path.split("/")[-1]]
        else:
          return self.paths[path]


    def mkdir(self, path):
        directs = path.split("/")

        for i in range(1, len(directs)):
          curr = "/".join(directs[:i]) or "/"

          if curr not in self.paths or directs[i] not in self.paths[curr]:
            bisect.insort(self.paths[curr], directs[i])


    def addContentToFile(self, filePath, content):
        if filePath not in self.paths:
          self.mkdir(filePath)
        self.files[filePath] += content


    def readContentFromFile(self, filePath):
        return self.files[filePath]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)