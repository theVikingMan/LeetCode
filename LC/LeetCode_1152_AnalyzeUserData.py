import collections
import itertools

def mostVisitedPattern(username, timestamp, website):
  rawAllData = [[user, time, site] for user, time, site in zip(username, timestamp, website)]
  sortedAllData = sorted(rawAllData, key=lambda i:(i[0], i[1]))

  options = collections.defaultdict(list)
  for user, _, site in sortedAllData:
    options[user].append(site)

  counts = collections.defaultdict(int)
  for user, sites in options.items():
    combos = set(itertools.combinations(sites, 3))
    for poss in combos:
      counts[poss] += 1

  maxVal, res = max(counts.values()), []
  for poss, count in counts.items():
    if count == maxVal:
      res.append(poss)

  if len(res) > 1:
    res.sort()

  return res[0]



username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
print(mostVisitedPattern(username, timestamp, website))