def dailyTemperatures(temperatures):
  res = [0] * len(temperatures)
  stack = []

  for i, t in enumerate(temperatures):
    while stack and t > stack[-1][0]:
      temp, idx = stack.pop()
      res[idx] = i - idx
    stack.append([t, i])
  return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))