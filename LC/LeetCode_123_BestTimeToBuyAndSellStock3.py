def solution(prices):
  t1_cost, t2_cost = float('inf'), float('inf')
  t1_profit, t2_profit = 0, 0

  for price in prices:
      # the maximum profit if only one transaction is allowed
      t1_cost = min(t1_cost, price)
      t1_profit = max(t1_profit, price - t1_cost)
      # reinvest the gained profit in the second transaction which dips negative but will
      # come back positive if another profit can be made in the second transaction
      t2_cost = min(t2_cost, price - t1_profit)
      t2_profit = max(t2_profit, price - t2_cost)

  return t2_profit

print(solution([3,2,6,7,0,3]))