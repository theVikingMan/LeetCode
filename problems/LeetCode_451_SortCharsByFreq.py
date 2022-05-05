def frequencySort(self, s):
    count = collections.Counter(s)
    freq = [[] for _ in range(len(s) + 1)]
    res = ''

    for char, cnt in count.items():
        freq[cnt].append(char)

    for i in range(len(freq) - 1, -1, -1):
        for let in freq[i]:
            res += let * i

    return res

print(frequencySort("Aabb"))