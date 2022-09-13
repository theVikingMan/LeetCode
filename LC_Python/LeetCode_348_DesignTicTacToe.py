import collections

# ------------ Initial solution (valid) ----------- #

class TicTacToe(object):
    def __init__(self, n):
      self.board = [[-1 for _ in range(n)] for _ in range(n)]
      self.hasWinner = False
      self.winner = None
      self.player1Row = collections.defaultdict(int)
      self.player1Col = collections.defaultdict(int)
      self.player1Pos = collections.defaultdict(int)
      self.player1Neg = collections.defaultdict(int)
      self.player2Row = collections.defaultdict(int)
      self.player2Col = collections.defaultdict(int)
      self.player2Pos = collections.defaultdict(int)
      self.player2Neg = collections.defaultdict(int)
      self.pieces = ['X', 'O']


    def move(self, row, col, player):
      player1 = {
        'piece': self.pieces[0],
         'rows' : self.player1Row,
         'cols' : self.player1Col,
         'pos' : self.player1Pos,
         'neg' : self.player1Neg,
      }
      player2 = {
        'piece': self.pieces[1],
         'rows' : self.player2Row,
         'cols' : self.player2Col,
         'pos' : self.player2Pos,
         'neg' : self.player2Neg,
      }
      if self.hasWinner:
        return 0

      competitor = player1 if player == 1 else player2
      if self.board[row][col] == -1 and 0 <= row < len(self.board) and 0 <= col < len(self.board):
        self.board[row][col] = competitor['piece']
        competitor['rows'][row] += 1
        competitor['cols'][col] += 1
        competitor['pos'][row + col] += 1
        competitor['neg'][row - col] += 1

      if competitor['rows'][row] == len(self.board) or competitor['cols'][col] == len(self.board) or competitor['pos'][row + col] == len(self.board) or competitor['neg'][row - col] == len(self.board):
        self.hasWinner = True
        self.winner = player
        return player
      return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)