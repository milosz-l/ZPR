import pygame
import random
from time import sleep

CELL_SIZE = 15

class BoardWindow:
    def __init__(self, height, width, states, cell_size=CELL_SIZE):
        self.height = height
        self.width = width
        self.states = states
        self.cell_size=cell_size
        self.window= pygame.display.set_mode((width * cell_size, height * cell_size))
        self.colors=define_colors(states)

    def update(self, new_board):
        for y in range(self.height):
            for x in range(self.width):
                new_rect = pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.window, self.colors[new_board[y][x]], new_rect)


def new_board(states, height, width):
    board = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            board[y][x]=random.randint(0, states-1)
    return board


def define_colors(states):
    COLORS=[(0, 0, 0) for _ in range(states)]
    R, G, B = (0, 0, 0)
    for i in range(states):
        COLORS[i]=(R, G, B)
        B+=255//(states-1)
    return COLORS


def main():
    pygame.init()
    STATES = 12
    height = 45
    width = 60
    board = GUIBoard(height, width, STATES)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        new_version=new_board(STATES, height, width)
        board.update(new_version)
        sleep(0.5)
        pygame.display.flip()

if __name__=="__main__":
    main()
