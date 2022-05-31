import heapq

def kClosest(self, points, k):
    minHeap = []
    res = []
    for x, y in points:
        dis = self.distance(x, y)
        minHeap.append([dis, x, y])
    heapq.heapify(minHeap)

    while k > 0:
        k -= 1
        dis, x, y = heapq.heappop(minHeap)
        res.append([x, y])
    return res

def distance(self, x, y):
    return x**2 + y**2