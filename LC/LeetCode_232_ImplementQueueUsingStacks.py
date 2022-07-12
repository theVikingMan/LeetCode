class MyQueue(object):

  def __init__(self):
    self.inStack = []
    self.outStack = []

  def push(self, x):
    self.inStack.append(x)


  def pop(self):
    res = self.peek()
    return self.outStack.pop()

  def peek(self):
    if len(self.outStack) == 0:
      while self.inStack:
        top = self.inStack.pop()
        self.outStack.append(top)
    return self.outStack[-1]


  def empty(self):
    return len(self.inStack) == 0 and len(self.outStack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()