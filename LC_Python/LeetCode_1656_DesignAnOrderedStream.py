class OrderedStream(object):

    def __init__(self, n):
      self.table = {}
      self.pnt = 1


    def insert(self, idKey, value):
      if idKey not in self.table:
        res = []
        self.table[idKey] = value
        if idKey == self.pnt:
          length = 0
          while self.pnt + length in self.table:
            res.append(self.table[self.pnt + length])
            length += 1
          self.pnt += length
      return res