def solution(startWords, targetWords):
  sWords = set()
  res = 0

  for w in startWords:
    wSorted = "".join(sorted(w))
    sWords.add(wSorted)

  for w in targetWords:
    wS = "".join(sorted(w))
    for i in range(len(wS)):
      prev = wS[:i] + wS[i+1:]
      if prev in sWords and wS[i] not in prev:
        res += 1
        break

  return res

print(solution(["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"],
                ["r","am","jg","umhjo","fov","lujy","b","uz","y"]))