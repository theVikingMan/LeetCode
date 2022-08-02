import collections, heapq

def topKFrequent(words, k):
    count = collections.Counter(words)
    freq = [[] for _ in range(len(words) + 1)]
    res = []

    for w, c in count.items():
        freq[c].append(w)

    for i in range(len(freq) - 1, -1, -1):
        freq[i].sort()
        for j in freq[i]:
            res.append(j)
            if len(res) == k:
              return res

print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))



# --------------------- Heap approach --------------------- #

def topKFrequent(words, k):
  heap = []
  count = collections.Counter(words)
  for w, cnt in count.items():
    heapq.heappush(heap, [-cnt, w])

  res = []
  while k:
    count, word = heapq.heappop(heap)
    res.append(word)
    k -= 1
  return res