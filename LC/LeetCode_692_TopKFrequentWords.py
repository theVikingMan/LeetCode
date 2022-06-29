def topKFrequent(self, words, k):
    count = {}
    freq = [[] for _ in range(len(words) + 1)]
    res = []

    for w in words:
        count[w] = 1 + count.get(w, 0)
    for w, c in count.items():
        freq[c].append(w)

    for i in range(len(freq) - 1, -1, -1):
        freq[i].sort()
        for j in freq[i]:
            res.append(j)
    return res[:k]

print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))