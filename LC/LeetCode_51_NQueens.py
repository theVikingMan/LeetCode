def solveNQueens(n):
    # create our constraint trackers. Remember, we are looping over the rows
    columns = set()
    posDiag = set() # (r + c)
    negDiag = set() # (r - c)

    #create result and board
    result = []
    board = [['.'] * n for i in range(n)]

    # create recursive function
    def backtrack(r):
        # base case if you have hit the end of the board
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        # loop through the columns as possible first starting positions
        for c in range(n):
            #base caseish
            if c in columns or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # if valid spot to place a piece, add it to the seen vars
            columns.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            # recursive call to move to the next row
            backtrack(r + 1)

            # clean up as usual with back tracking problems
            columns.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    # start at the first row
    backtrack(0)
    return result

print(solveNQueens(4))