import pygame
import tkinter as tk
from tkinter import *
from board_display import BoardWindow
import random

class UserOptions:
    def __init__(self, width=100, height=100):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root, width = width, height = height)
        self.frame.pack(side = LEFT)
        self.start_button = Button(self.frame,text = 'Start',  command=self.start)
        self.start_button.pack(side=LEFT)
        self.stop_button = Button(self.frame,text = 'Stop',  command=self.stop)
        self.stop_button.pack(side=LEFT)
        self.root.update()

    def start(self):
        STATES = 12
        height = 45
        width = 60
        self.board = BoardWindow(height, width, STATES)
        self.run()

    def run(self):
        STATES = 12
        height = 45
        width = 60
        while True:
            new_version=new_board(STATES, height, width)
            self.board.update(new_version)
            pygame.display.flip()
            self.root.update()

    def stop(self):
        pygame.quit()


def new_board(states, height, width):
    board = [[0 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            board[y][x]=random.randint(0, states-1)
    return board

game = UserOptions()
while True:
    game.root.update()

# https://stackoverflow.com/questions/23319059/embedding-a-pygame-window-into-a-tkinter-or-wxpython-frame
