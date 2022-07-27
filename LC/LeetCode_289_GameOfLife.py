
# --------------- O(1) space Solution ---------------- #
def gameOfLife(self, board):
    #  Original |  New   | State
    #     0     |   0    |   0
    #     1     |   0    |   1
    #     0     |   1    |   2
    #     1     |   1    |   3

    ROWS, COLS = len(board), len(board[0])

    def countNei(r, c):
        nei = 0
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                    continue
                if board[i][j] in [1, 3]:
                    nei += 1
        return nei

    for r in range(ROWS):
        for c in range(COLS):
            nei = countNei(r, c)
            if board[r][c]:
                if nei in [2, 3]:
                    board[r][c] = 3
            elif nei == 3:
                board[r][c] = 2

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2, 3]:
                board[r][c] = 1

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

# def gameOfLife(board):
#     # nei == 3 : 0 --> 1 : rebirth
#     # 2 <= nei <= 3 : 1 --> 1 : still alive
#     # nei < 2 : 1 --> 0 : dead
#     # nei > 3 : 1 --> 0 : dead
#     ROWS, COLS = len(board), len(board[0])

#     res = [ [0 for c in range(COLS)] for r in range(ROWS) ]

#     def helper(r, c):
#         total = 0
#         directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
#         for rDir, cDir in directions:
#             total += board[r + rDir][c + cDir] if (r + rDir >= 0 and c + cDir >= 0 and r + rDir != ROWS and c + cDir != COLS) else 0

#         if total == 3:
#             res[r][c] = 1
#         elif total == 2 and board[r][c] == 1:
#             res[r][c] = 1
#         elif total < 2 or total > 3:
#             res[r][c] = 0


#     for r in range(ROWS):
#         for c in range(COLS):
#             helper(r, c)
#     for r in range(ROWS):
#         for c in range(COLS):
#             board[r][c] = res[r][c]

#     return board