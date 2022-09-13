import heapq

class StockPrice:
    def __init__(self):
        self.timeStamps = {}
        self.mostRecentTime = 0
        self.maxPrice = []
        self.minPrice = []
        heapq.heapify(self.maxPrice)
        heapq.heapify(self.minPrice)

    def update(self, timestamp: int, price: int) -> None:
      # update exisiting records
      self.timeStamps[timestamp] = price
      self.mostRecentTime = max(self.mostRecentTime, timestamp)

      # Update heaps
      heapq.heappush(self.maxPrice, (-price, timestamp))
      heapq.heappush(self.minPrice, (price, timestamp))

    def current(self) -> int:
      return self.timeStamps[self.mostRecentTime]

    def maximum(self) -> int:
      currPrice, time = heapq.heappop(self.maxPrice)
      while -currPrice != self.timeStamps[time]:
        currPrice, time = heapq.heappop(self.maxPrice)

      heapq.heappush(self.maxPrice, (currPrice, time))
      return -currPrice

    def minimum(self) -> int:
      currPrice, time = heapq.heappop(self.minPrice)
      while currPrice != self.timeStamps[time]:
        currPrice, time = heapq.heappop(self.minPrice)

      heapq.heappush(self.minPrice, (currPrice, time))
      return currPrice



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()