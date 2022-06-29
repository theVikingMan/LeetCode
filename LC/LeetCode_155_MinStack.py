class MinStack:
    def __init__(self):
        self.s = []
        self.prevMinElems = []
        self.currMinElem = float('inf')

    def push(self, val: int) -> None:
        self.s.append(val)
        if val <= self.currMinElem:
          self.prevMinElems.append(self.currMinElem)
          self.currMinElem = val

    def pop(self) -> None:
        topElemRemv = self.s.pop()
        if topElemRemv == self.currMinElem:
          self.currMinElem = self.prevMinElems.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.currMinElem


# Your MinStack object will be instantiated and called as such:
# obj = MinStack(): null
# obj.push(val): null
# obj.pop(): null
# param_3 = obj.top(): int
# param_4 = obj.getMin(): int