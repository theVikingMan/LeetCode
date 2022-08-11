import collections, heapq

transaction_data = [
  ["Purchase", "Starbucks", 9.99, "02032022"],
  ["Purchase", "Starbucks", 11.01, "02042022"],
  ["Purchase", "Starbucks", 10.99, "03032022"],
  ["Purchase", "McDonalds", 1.00, "02032022"],
  ["Purchase", "McDonalds", 2.00, "04032022"],
  ["Purchase", "McDonalds", 100.00, "04102022"],
  ["Purchase", "Macy's", 200.00, "04102023"],
  ["Refund", "Macy's", 190.00, "04122023"],
]

cash_back = [
  ["Starbucks", 0.02],
  ["McDonalds", 0.03],
  ["Macy's", 0.025],
]

class Solution:
  def __init__(self):
    self.trans_history = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
    self.cashback_history = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))


  def uploadData(self, transDataSet, cashDataSet):
    dictCashBackOffers = {}
    for company, rate in cashDataSet:
      dictCashBackOffers[company] = rate

    for typeOf, company, amount, date in transDataSet:
      monthYear = date[0:2] + date[-4:]
      if typeOf == "Purchase":
        self.trans_history[monthYear][company] = amount + self.trans_history[monthYear][company]
        self.cashback_history[monthYear][company] = (amount * dictCashBackOffers[company])+ self.cashback_history[monthYear][company]
      elif typeOf == "Refund":
        self.trans_history[monthYear][company] = self.trans_history[monthYear][company] - amount
        self.cashback_history[monthYear][company] = self.cashback_history[monthYear][company] - (amount * dictCashBackOffers[company])

    return True


  def print_data(self):
    print("------- Total amount spent -------")
    for date, data in self.trans_history.items():
      for company, total in data.items():
        print(f"{company}: {total} on {date}")

    print("\n------- Cash Back Offers -------")
    for date, data in self.cashback_history.items():
      for company, total in data.items():
        print(f"{company}: {total} on {date}")


  def calc_top_N(self, n, dateToPull):
    maxHeap = []
    for company, total in self.cashback_history[dateToPull].items():
      heapq.heappush(maxHeap, [-total, company])

    place = 1
    while n and len(maxHeap) > 0:
      total, company = heapq.heappop(maxHeap)
      print(f"({place}) {-total}: {company}")
      place += 1

    return True



example1 = Solution()
example1.uploadData(transaction_data, cash_back)
example1.print_data()
example1.calc_top_N(2, "032022")