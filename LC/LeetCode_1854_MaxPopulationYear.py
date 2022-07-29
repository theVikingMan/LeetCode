def maximumPopulation(logs):
  birth = [b for b, d in sorted(logs, key=lambda i:i[0])]
  death = [d for b, d in sorted(logs, key=lambda i:i[1])]

  res = curr = bP = dP = 0
  year = float('inf')

  while bP < len(birth):
    if birth[bP] < death[dP]:
      curr += 1
      if curr > res:
        res = curr
        year = birth[bP]
      bP += 1
    else:
      curr -= 1
      dP += 1

  return year

print(maximumPopulation([[1950,1961],[1960,1971],[1970,1981]]))