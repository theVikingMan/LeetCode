import heapq

def lastStoneWeight(stones):
    heap = [-wght for wght in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        elem1 = heapq.heappop(heap)
        elem2 = heapq.heappop(heap)
        heapq.heappush(heap, elem1 - elem2)

    return heapq.heappop(heap) * -1

print(lastStoneWeight([2,7,4,1,8,1]))