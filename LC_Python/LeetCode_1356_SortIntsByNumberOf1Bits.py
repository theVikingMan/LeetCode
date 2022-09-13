import collections

class Solution:
  def sortByBits(self, arr):
    bitCount = collections.defaultdict(list)
    for n in arr:
      bitCount[self.getBitCount(n)].append(n)

    res = []
    for i in range(15):
      if bitCount[i]:
        res.extend(sorted(bitCount[i]))
    return res

  def getBitCount(self, num):
    bitRep = bin(num)[2:]
    res = 0
    for dig in bitRep:
      res += 1 if dig == "1" else 0
    return res