

import random

class GameBoard:
  def __init__(self, board_size):
    self.board = [[" " for _ in range(board_size)] for _ in range(board_size)]

  def letter_to_number(self, letter):
    letter_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
    return letter_dict[letter]

  def print_board(self):
    print('  A B C D E F G H')
    print('  +-+-+-+-+-+-+-+')
    row_num = 1
    for row in self.board:
      printed_row = '|'.join(row)
      print(f'{row_num}| {printed_row}')
      row_num += 1


class Battleship:
  def __init__(self, board):
    self.board = board

  def create_computer_ships(self):
    for _ in range(5): # only can have 5 ships
      self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
      while self.board[self.x_row][self.y_column] == 'X':
        self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
      self.board[self.x_row][self.y_column] = 'X'
    return self.board

  def count_hit_ships(self):
    hit_ships = 0
    ROWS, COLS = len(self.board), len(self.board[0])
    for r in range(ROWS):
      for c in range(COLS):
        if self.board[r][c] == 'X':
          hit_ships += 1
    return hit_ships


class Player:
  def __init__(self, name):
    self.name = name

  def get_user_input(self):
    try:
      x_row = input('Enter the row of the ship: ')
      while x_row not in '12345678':
        print('Not a valid row, please select a valid row number')
        x_row = input('Enter the row of the ship: ')

      y_column = input('Enter the column of the ship: ').upper()
      while y_column not in 'ABCDEFGH':
        print('Not a valid column, please select a valid column number')
        y_column = input('Enter the column of the ship: ')
      return int(x_row) - 1, GameBoard.letter_to_number(y_column)
    except ValueError and KeyError:
      print('Not a valid input')
      return self.get_user_input()


board_computer = GameBoard(8)
board_player = GameBoard(8)

battleship_computer = Battleship(board_computer)
battleship_computer.create_computer_ships()
