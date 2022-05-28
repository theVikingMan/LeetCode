import collections

# ---------------- Bucket Sort ---------------- #
def frequencySort(s):
    count = collections.Counter(s) # get the count for all the letters
    freq = [[] for _ in range(len(s) + 1)] # will need 0 - length of array slots
    res = ''

    for char, cnt in count.items(): # place the letters in the bucket at the count idx
        freq[cnt].append(char)

    for i in range(len(freq) - 1, -1, -1): # work from highest idx to lowest
        for let in freq[i]:
            res += let * i # Magic way to solve the problem. Just add all the same number of
                           # letters to the res

    return res

print(frequencySort("cabb"))