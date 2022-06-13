import collections, heapq

# ----------- Bucket Sort Solution ----------- #
def topKFrequents(nums, k):
    count = {} # count occurances of numbers
    freq = [[] for _ in range(len(nums) + 1)]

    for n in nums: # for loop to count all item occurances
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items(): # add number to the frequency array, tracking how many times a num is seen
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequents([1,1,1,2,2,3], 2))


# ----------- Heap Solution ----------- #
# def topKFrequent(nums, k):
#     count = collections.Counter(nums)
#     heap = [[-cnt, num] for num, cnt in count.items()]
#     res = []
#     heapq.heapify(heap)

#     while k:
#         k -= 1
#         top = heapq.heappop(heap)
#         res.append(top[1])

#     return res

# print(topKFrequent([1,1,1,2,2,2,3], 2))