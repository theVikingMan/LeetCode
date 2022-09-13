
def minHeightShelves(books, shelfWidth):
  dp = {}

  def helper(i, maxH, currW):
    if currW < 0:
      return float('inf')
    if i == len(books):
      return maxH

    if (i, maxH, currW) in dp:
      return dp[(i, maxH, currW)]

    same = helper(i + 1, max(maxH, books[i][1]), currW - books[i][0])
    nxt = maxH + helper(i + 1, books[i][1], shelfWidth - books[i][0])

    dp[(i, maxH, currW)] = min(same, nxt)
    return dp[(i, maxH, currW)]

  return helper(0, 0, 0)

print(minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))

# ------------------ Base recursive (TLE) ------------ #

def minHeightShelves(books, shelfWidth):
  dp = {}

  def helper(i, w, maxH, totalH):
    if i == len(books):
      return totalH + maxH

    outcome = float('inf')

    if w + books[i][0] <= shelfWidth:
      outcome = min(outcome, helper(i + 1, w + books[i][0], max(maxH, books[i][1]), totalH))
    outcome = min(outcome, helper(i + 1, books[i][0], books[i][1], totalH + maxH))

    return outcome

  return helper(0, 0, 0, 0)