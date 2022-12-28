import pygame
from board import Board
from game import Game
import sys
import math

# Defines color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Defines the size of the game window
WIDTH = 700
HEIGHT = 600 + 100

# Defines the size of each cell
CELL_SIZE = 100

# Initialize pygame
pygame.init()

# Creates the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Sets the title of the game window
pygame.display.set_caption("Connect 4")

# Initializes the font constant
FONT = pygame.font.SysFont("monospace", 75)

# Creates the main board object and game object, and draws the starting board
b = Board()
game = Game(b, 'R', 'Y')
game.draw_board(window, BLUE, BLACK, RED, YELLOW)

# Creates the main game loop, that breaks when the game is over
switch = 0
while not game.is_over():

    # Creates a loop that goes through all pygame "events" (player actions)
    for event in pygame.event.get():

        # If a player hits the x in the top corner, the window disappears and the game ends
        if event.type == pygame.QUIT:
            sys.exit()

        # Enter the if statement when the cursor moves
        if event.type == pygame.MOUSEMOTION:

            # Redraws a black rectangle in the space above the board
            pygame.draw.rect(window, BLACK, (0, 0, WIDTH, 100))
            pygame.display.update()

            # Draws a circle that follows the cursor on the x-axis above the board and changes color depending on turn
            x_pos = event.pos[0]
            if(switch%2 == 0):
                pygame.draw.circle(window, RED, (x_pos, 50), 45)
                pygame.display.update()
            else:
                pygame.draw.circle(window, YELLOW, (x_pos, 50), 45)
                pygame.display.update()

        # Enters the if statement when the player clicks down on the mouse pad
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_valid = False

            # If it is player one's turn, enters the if statement
            if(switch%2 == 0):

                # Selects the column based on cursor x position
                x_pos = event.pos[0]
                selection = int(math.floor(x_pos/100)) + 1

                # If the column has empty rows, enters the if statement and updates the board
                if(game.board.is_valid_location(selection)):
                    row = game.board.row_pos(selection)
                    game.board.update_board(row, selection - 1, game.team1)
                    is_valid = True

            # If it is player two's turn, enters the if statement
            if(switch%2 == 1):

                # Selects the column based on cursor x position
                x_pos = event.pos[0]
                selection = int(math.floor(x_pos / 100)) + 1

                # If the column has empty rows, enters the if statement and updates the board
                if (game.board.is_valid_location(selection)):
                    row = game.board.row_pos(selection)
                    game.board.update_board(row, selection - 1, game.team2)
                    is_valid = True

            # Updates board visual after each turn
            game.draw_board(window, BLUE, BLACK, RED, YELLOW)

            # Updates the turn after a player makes a valid move
            if(is_valid == True):
                switch += 1

# If Player 2 won, display it to the window
if(switch%2 == 0):
    pygame.draw.rect(window, BLACK, (0, 0, WIDTH, 100))
    label = FONT.render("Player 2 Wins!", 1, YELLOW)
    window.blit(label, (40, 10))
    pygame.display.update()

# If Player 1 won, display it to the window
else:
    pygame.draw.rect(window, BLACK, (0, 0, WIDTH, 100))
    label = FONT.render("Player 1 Wins!", 1, RED)
    window.blit(label, (40, 10))
    pygame.display.update()

# Hold the screen for 5 seconds after displaying the message
pygame.time.wait(5000)