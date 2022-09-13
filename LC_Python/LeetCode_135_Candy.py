
# ---------- Two Pass ------ #

def candy(ratings):
  dp = [1 for _ in range(len(ratings))]

  for i in range(1, len(ratings)):
    if ratings[i] > ratings[i-1]:
      dp[i] = max(dp[i], dp[i-1] + 1)

  for i in range(len(ratings) - 2, -1, -1):
    if ratings[i] > ratings[i+1]:
      dp[i] = max(dp[i], dp[i+1] + 1)

  return sum(dp)


# ---------- Valley / Peak Finding ----- #

def candy(ratings):
    bounds = [-1, len(ratings)]
    res = [0 for _ in range(len(ratings))]

    for i, score in enumerate(ratings):
        if (i - 1 in bounds or ratings[i-1] >= score) and (i + 1 in bounds or ratings[i+1] >= score):
            l, r = i - 1, i + 1
            res[i] = 1
            while l >= 0 and ratings[l] > ratings[l + 1]:
                res[l] = max(res[l], res[l+1] + 1)
                l -= 1
            while r < len(ratings) and ratings[r] > ratings[r - 1]:
                res[r] = max(res[r], res[r-1] + 1)
                r += 1
    return sum(res)

print(candy([1,0,2]))
print(candy([1,2,2]))