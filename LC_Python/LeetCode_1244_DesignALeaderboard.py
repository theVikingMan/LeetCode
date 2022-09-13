import heapq

class Leaderboard(object):
    def __init__(self):
        self.scores = {}

    def addScore(self, playerId, score):
        if playerId not in self.scores:
          self.scores[playerId] = 0
        self.scores[playerId] += score


    def top(self, K):
        heap = []
        for player, score in self.scores.items():
          heapq.heappush(heap, -score)

        res = 0
        while K:
          res += heapq.heappop(heap)
          K -= 1
        return res * -1


    def reset(self, playerId):
        self.scores[playerId] = 0