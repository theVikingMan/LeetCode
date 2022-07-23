class RandomizedSet(object):
    def __init__(self):
      self.dict = {}
      self.list = []

    def insert(self, val):
      if val not in self.dict:
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
      return False


    def remove(self, val):
      if val not in self.dict :
        return False
      # Basically over write the to-del val instead of swapping
      valIdx, lastElem = self.dict[val], self.list[-1]
      self.dict[lastElem], self.list[valIdx] = valIdx, lastElem
      self.list.pop()
      del self.dict[val]
      return True


    def getRandom(self):
      return self.list[random.randint(0, len(self.list) - 1)]