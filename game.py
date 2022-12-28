from board import Board
import pygame

class Game:

    # Initializes Game Object
    def __init__(self, b, team1, team2):
        self.board = b
        self.team1 = team1
        self.team2 = team2

    # Checks if the game is over using the is_4 function, True if over, and False if not
    def is_over(self):
        if(self.board.is_4(self.team1) == True or self.board.is_4(self.team2) == True):
            return True
        else:
            return False

    # Allows a player to make a move by getting the row_idx, and using the update_board function
    def make_move(self, col_num):
        col_idx = col_num - 1
        row_idx = self.board.row_pos(self.board, col_num)
        self.board.update_board(self.board, row_idx, col_idx)

    # Uses pygame to draw the board, setting a background color, and creating the actual board
    def draw_board(self, screen, board_color, e_circle_color, r_circle_color, y_circle_color):
        for col in range(7):
            for row in range(6):
                pygame.draw.rect(screen, board_color, (col*100, row*100 + 100, 100, 100))
                if(self.board.board[row][col] == "O"):
                    pygame.draw.circle(screen, e_circle_color, (col*100 + 50, row*100 + 100 + 50), 45)
                elif (self.board.board[row][col] == "R"):
                    pygame.draw.circle(screen, r_circle_color, (col * 100 + 50, row * 100 + 100 + 50), 45)
                elif (self.board.board[row][col] == "Y"):
                    pygame.draw.circle(screen, y_circle_color, (col * 100 + 50, row * 100 + 100 + 50), 45)
        pygame.display.update()


