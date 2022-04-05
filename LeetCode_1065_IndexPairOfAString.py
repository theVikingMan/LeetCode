def indexPairs(text, words):
    res = []
    n = len(text)
    for i in range(n):
        for w in words:
            j = i + len(w)
            pontWord = text[i:j]
            if j < n and pontWord == w:
                res.append([i, j-1])
    res.sort()
    return res

print(indexPairs("thestoryofleetcodeandme", ["story","fleet","leetcode"]))