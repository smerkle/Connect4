import numpy as np

class Board:

    # Initializes Board Object
    def __init__(self):
        self.board = np.array([["O", "O", "O", "O", "O", "O", "O"],
                               ["O", "O", "O", "O", "O", "O", "O"],
                               ["O", "O", "O", "O", "O", "O", "O"],
                               ["O", "O", "O", "O", "O", "O", "O"],
                               ["O", "O", "O", "O", "O", "O", "O"],
                               ["O", "O", "O", "O", "O", "O", "O"]])

    # Returns the dimensions of the board when printed
    def __str__(self):
        return f"6x7 connect 4 board"

    # Prints out the actual board, with the pieces in each row
    def print_board(self):
        for row in self.board:
            for space in row:
                print(str(space), end='')
            print("\n")

    # Finds the next available
    def row_pos(self, col):

        # goes through each row for the specified column, and checks for a Red or Yellow piece
        for i in range(len(self.board)):
            if(self.board[i][int(col) - 1] != "O"):
                free_row_idx = i - 1
                return free_row_idx

        # If no pieces are in the column, returns the index for the bottom row
        return 5

    # Checks if the selected column by the user is valid, if it is all full, it is invalid and returns false
    def is_valid_location(self, col):
        if(self.board[0][int(col) - 1] != "O"):
            return False
        else:
            return True

    # Updates the board, with the row, column, and specified team
    def update_board(self, row_idx, col_idx, team):
        self.board[row_idx][col_idx] = team

    # Checks if there are 4 pieces of the same color in a row on the board, returns True if there are, and False if not
    def is_4(self, team):
        streak = 1
        is_4 = False

        # Checks if there are four in a row within the rows
        for i in range(len(self.board)):
            for j in range(1, len(self.board[i])):
                if(self.board[i][j] == team and self.board[i][j - 1] == team):
                    streak += 1
                    if(streak >= 4):
                        is_4 = True
                        return is_4
                else:
                    streak = 1
            streak = 1

        # Checks if there are four in a row within the columns
        streak = 1
        for i in range(len(self.board[0])):
            for j in range(1, len(self.board)):
                if(self.board[j][i] == team and self.board[j - 1][i] == team):
                    streak += 1
                    if(streak >= 4):
                        is_4 = True
                        return is_4
                else:
                    streak = 1
            streak = 1

        diagonals = []

        # Gets the upper right to lower left diagonals
        diags = [self.board[::-1, :].diagonal(i) for i in range(-self.board.shape[0] + 1, self.board.shape[1])]

        # Gets the upper left to lower right diagonals
        diags.extend(self.board.diagonal(i) for i in range(self.board.shape[1] - 1, -self.board.shape[0], -1))

        # Creates a list of lists holding all diagonal sequences
        [diagonals.append(n.tolist()) for n in diags]

        # Checks if there are four in a row within the diagonals
        streak = 1
        for i in range(len(diagonals)):
            if(len(diagonals[i]) > 1):
                for j in range(1, len(diags[i])):
                    if(diagonals[i][j] == team and diagonals[i][j - 1] == team):
                        streak += 1
                        if (streak >= 4):
                            is_4 = True
                            return is_4
                    else:
                        streak = 1
                streak = 1
        return is_4