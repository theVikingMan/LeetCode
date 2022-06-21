import heapq

def kClosest(points, k):
    minHeap = []
    res = []
    for x, y in points: # generate distances for each coord
        dis = distance(x, y)
        minHeap.append([dis, x, y])
    heapq.heapify(minHeap) # heapify based on calc (python is default inHeap)

    while k > 0:
        k -= 1
        dis, x, y = heapq.heappop(minHeap)
        res.append([x, y])
    return res

def distance(x, y):
    return x**2 + y**2